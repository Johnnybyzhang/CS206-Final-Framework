#!/usr/bin/env python3
"""Generate structured quadratic voting transcripts via an OpenAI-compatible endpoint.

This script keeps the original `llm_transcripts.md` output location but produces
nested (two-layer) sections keyed by country and entry index. Credits are sampled
from ``[0, 1, 4, 9]`` while ensuring that the value ``9`` appears at most twice
across the entire run. When credits are positive, a transcript is requested from
an OpenAI-compatible chat-completions endpoint using a command-line supplied API
key.

Example usage:

```
python generate_llm_transcripts_structured.py \
    --api-key $OPENAI_API_KEY \
    --endpoint https://api.openai.com/v1/chat/completions \
    --model gpt-5
```
```"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Iterable, List, Sequence

import requests

DEFAULT_COUNTRIES: Sequence[str] = (
    "USA",
    "China",
    "Germany",
    "India",
    "Brazil",
    "UK",
    "France",
    "Japan",
    "Canada",
    "Australia",
)
CREDIT_OPTIONS: Sequence[int] = (0, 1, 4, 9)
MAX_NINES = 2


class TranscriptGenerationError(RuntimeError):
    """Raised when the LLM transcript cannot be generated."""


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create structured LLM transcripts for quadratic voting scenarios."
    )
    parser.add_argument(
        "--api-key",
        required=True,
        help="API key for an OpenAI-compatible endpoint (passed as Bearer token).",
    )
    parser.add_argument(
        "--endpoint",
        default="https://api.openai.com/v1/chat/completions",
        help="Chat completions endpoint URL (default: %(default)s)",
    )
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        help="Model identifier understood by the endpoint (default: %(default)s)",
    )
    parser.add_argument(
        "--countries",
        nargs="*",
        default=list(DEFAULT_COUNTRIES),
        help=(
            "Optional custom list of countries. Provide as space-separated names; "
            "defaults to %(default)s"
        ),
    )
    parser.add_argument(
        "--entries-per-country",
        type=int,
        default=2,
        help="Number of transcript entries to generate per country (default: %(default)s)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Seed the RNG for reproducible credit assignment.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "llm_transcripts.md",
        help="Output Markdown path (default: %(default)s)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="HTTP request timeout in seconds (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Generate the structure without calling the LLM (for testing).",
    )
    return parser


def select_credit(options: Sequence[int], rng: random.Random, nines_left: int) -> int:
    chosen = rng.choice(options)
    if chosen == 9 and nines_left <= 0:
        # Re-sample without the value 9 if we've exhausted the allowance.
        allowed_options = [value for value in options if value != 9]
        if not allowed_options:
            raise ValueError("No non-9 credit options available to select from.")
        chosen = rng.choice(allowed_options)
    return chosen


def request_llm_transcript(
    endpoint: str,
    api_key: str,
    model: str,
    prompt: str,
    timeout: float,
) -> str:
    response = requests.post(
        endpoint,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=timeout,
    )
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:  # pragma: no cover - thin wrapper
        raise TranscriptGenerationError(
            f"HTTP error {response.status_code}: {response.text.strip()}"
        ) from exc

    payload = response.json()
    try:
        choice = payload["choices"][0]
        message = choice["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise TranscriptGenerationError(
            f"Unexpected response structure: {json.dumps(payload, indent=2)}"
        ) from exc
    return message.strip()


def build_prompt(country: str, credit: int, entry_index: int) -> str:
    return (
        "You are participating in a quadratic voting simulation. "
        f"The country is {country}. A voter has {credit} credits. "
        "Write a brief transcript of the voter's deliberation on how "
        "to allocate their credits across public issues, highlighting "
        "trade-offs, concerns, and final decisions."
        f"\n\nEntry index: {entry_index}"
    )


def format_transcript_markdown(
    country: str,
    entry_index: int,
    credit: int,
    transcript: str,
) -> str:
    heading = f"#### Entry {entry_index + 1}"
    metadata = f"*Credits*: {credit}"
    body = transcript if transcript else "(No transcript generated.)"
    return f"{heading}\n{metadata}\n\n{body}\n"


def write_transcripts(
    output_path: Path,
    country_sections: Iterable[str],
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        handle.write("# Quadratic Voting LLM Transcripts\n\n")
        for section in country_sections:
            handle.write(section)
            handle.write("\n")


def generate_transcripts(
    countries: Sequence[str],
    entries_per_country: int,
    rng: random.Random,
    endpoint: str,
    api_key: str,
    model: str,
    timeout: float,
    dry_run: bool,
) -> List[str]:
    country_sections: List[str] = []
    nines_remaining = MAX_NINES

    for country in countries:
        lines = [f"## {country}"]
        for entry_index in range(entries_per_country):
            credit = select_credit(CREDIT_OPTIONS, rng, nines_remaining)
            if credit == 9:
                nines_remaining = max(0, nines_remaining - 1)

            transcript_text = ""
            if credit > 0 and not dry_run:
                prompt = build_prompt(country, credit, entry_index)
                try:
                    transcript_text = request_llm_transcript(
                        endpoint=endpoint,
                        api_key=api_key,
                        model=model,
                        prompt=prompt,
                        timeout=timeout,
                    )
                except TranscriptGenerationError as exc:
                    transcript_text = f"Error: {exc}"
            elif credit == 0:
                transcript_text = (
                    "No credits assigned. Participant sits out this round."
                )
            else:  # dry-run
                transcript_text = (
                    "Dry-run mode: transcript not requested from LLM."
                )

            lines.append(
                format_transcript_markdown(
                    country=country,
                    entry_index=entry_index,
                    credit=credit,
                    transcript=transcript_text,
                )
            )
        country_sections.append("\n".join(lines))
    return country_sections


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    rng = random.Random(args.seed)
    transcripts = generate_transcripts(
        countries=args.countries,
        entries_per_country=args.entries_per_country,
        rng=rng,
        endpoint=args.endpoint,
        api_key=args.api_key,
        model=args.model,
        timeout=args.timeout,
        dry_run=args.dry_run,
    )

    write_transcripts(args.output, transcripts)

    print(
        f"Wrote {len(transcripts)} country sections to {args.output.relative_to(Path.cwd())}",
        flush=True,
    )


if __name__ == "__main__":  # pragma: no cover - script entry point
    main()
