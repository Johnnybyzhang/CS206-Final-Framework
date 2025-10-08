"""Generate publication-ready figures for the final proposal."""
from __future__ import annotations

import re
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "computational_scientist" / "results" / "auction_rounds.csv"
TRANSCRIPTS = ROOT / "mechanism_design" / "implementations" / "llm_transcripts.md"


def plot_revenue_by_round(df: pd.DataFrame, output: Path) -> None:
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(df["round_index"], df["revenue"], marker="o", linewidth=1.3, label="Second-price revenue")
    ax.set_xlabel("Round")
    ax.set_ylabel("Revenue (tokens)")
    ax.set_title("Revenue decays as bidder budgets tighten")
    ax.axhline(df["revenue"].mean(), color="#555555", linestyle="--", linewidth=1, label="Mean revenue")
    ax.legend(loc="upper right")
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300)
    plt.close(fig)


def plot_winner_curse_window(df: pd.DataFrame, output: Path) -> None:
    df = df.copy()
    df["curse"] = df["notes"].str.contains("winner's curse")
    df["window"] = ((df["round_index"] - 1) // 10 + 1).astype(int)
    agg = df.groupby("window")["curse"].mean().reset_index()

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(6, 4))
    color = sns.color_palette("mako", n_colors=1)[0]
    sns.barplot(data=agg, x="window", y="curse", ax=ax, color=color)
    ax.set_xlabel("Round window")
    ax.set_ylabel("Winner's curse frequency")
    ax.set_title("Behavioural deviations concentrate early")
    ax.set_ylim(0, 0.5)
    ax.yaxis.set_major_formatter(lambda y, _: f"{y:.0%}")
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300)
    plt.close(fig)


def parse_transcripts(path: Path) -> pd.DataFrame:
    credit_pattern = re.compile(r"\((\d+) credits\)")
    decision_pattern = re.compile(r"In line with '([^']+)'")

    credits = []
    decisions = []
    with path.open() as fh:
        for line in fh:
            credit_match = credit_pattern.search(line)
            if credit_match:
                credits.append(int(credit_match.group(1)))
            decision_match = decision_pattern.search(line)
            if decision_match:
                decisions.append(decision_match.group(1))

    length = min(len(credits), len(decisions))
    df = pd.DataFrame({"credits": credits[:length], "decision": decisions[:length]})
    return df


def plot_voting_heatmap(df: pd.DataFrame, output: Path) -> None:
    pivot = df.pivot_table(index="credits", columns="decision", aggfunc="size", fill_value=0)
    pivot = pivot.reindex(sorted(pivot.index))

    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(9, 4))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu", ax=ax, cbar=False)
    ax.set_title("Quadratic voting choices by veto-credit endowment")
    ax.set_xlabel("Decision")
    ax.set_ylabel("Credits")
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300)
    plt.close(fig)


def main() -> None:
    df = pd.read_csv(RESULTS)
    plot_revenue_by_round(df, ROOT / "visualizations" / "auctions" / "revenue_by_round.png")
    plot_winner_curse_window(df, ROOT / "visualizations" / "auctions" / "winners_curse_frequency.png")

    transcript_df = parse_transcripts(TRANSCRIPTS)
    plot_voting_heatmap(transcript_df, ROOT / "visualizations" / "voting" / "credit_option_heatmap.png")

    summary_counts = transcript_df.groupby("decision")["credits"].count().to_dict()
    summary_path = ROOT / "visualizations" / "voting" / "decision_summary.json"
    summary_path.write_text(pd.Series(summary_counts).to_json(indent=2))


if __name__ == "__main__":
    main()
