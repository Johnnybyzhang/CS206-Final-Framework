"""Simulate a repeated budget-constrained second-price auction with behavioural types."""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import List

import numpy as np


@dataclass
class BidderState:
    """Track a bidder's budget and bidding rule."""

    name: str
    budget: float
    strategy: str

    def bid(self, value: float, common_value: float | None = None) -> float:
        """Return a bid following the bidder's strategy."""
        if self.strategy == "rational_threshold":
            return min(value, self.budget)

        if self.strategy == "bounded_optimist":
            optimism = np.random.normal(loc=0.15, scale=0.05)
            optimistic_value = value * (1 + max(optimism, 0))
            bid = min(optimistic_value, self.budget)
            return float(np.clip(bid, 0, self.budget))

        if self.strategy == "cautious_conserver":
            discount = np.random.uniform(0.15, 0.35)
            return max(0.0, min(value * (1 - discount), self.budget))

        raise ValueError(f"Unknown strategy: {self.strategy}")


@dataclass
class AuctionResult:
    round_index: int
    winner: str | None
    winning_bid: float
    clearing_price: float
    revenue: float
    efficiency: float
    winner_value: float
    runner_up_value: float
    winner_budget_remaining: float
    notes: str


def draw_private_values(num_bidders: int, mean: float, std: float) -> np.ndarray:
    draws = np.random.lognormal(mean=mean, sigma=std, size=num_bidders)
    return draws


def run_simulation(
    num_rounds: int,
    bidders: List[BidderState],
    value_mean: float,
    value_sigma: float,
    common_value_weight: float,
    seed: int | None = None,
) -> list[AuctionResult]:
    rng = np.random.default_rng(seed)
    results: list[AuctionResult] = []

    for round_index in range(1, num_rounds + 1):
        private_values = draw_private_values(len(bidders), mean=value_mean, std=value_sigma)
        common_value = float(rng.lognormal(mean=value_mean, sigma=value_sigma))
        realised_values = (1 - common_value_weight) * private_values + common_value_weight * common_value

        bids = []
        for bidder, value in zip(bidders, realised_values):
            if bidder.strategy == "bounded_optimist":
                bid = bidder.bid(value, common_value=common_value)
            else:
                bid = bidder.bid(value)
            bids.append(bid)

        sorted_idx = np.argsort(bids)[::-1]
        highest = sorted_idx[0]
        second_highest = sorted_idx[1]

        winner = bidders[highest]
        runner_up_value = realised_values[second_highest]
        clearing_price = min(bids[second_highest], winner.budget)
        winning_bid = bids[highest]
        revenue = clearing_price

        allocative_efficiency = float(realised_values[highest] >= np.max(realised_values) - 1e-9)

        notes = []
        if winning_bid > realised_values[highest] and winner.strategy != "rational_threshold":
            notes.append("winner's curse style overbid")
        if winner.budget <= 1e-9:
            notes.append("budget exhausted")
        elif winner.budget < clearing_price:
            notes.append("budget binding")

        winner.budget -= clearing_price

        result = AuctionResult(
            round_index=round_index,
            winner=winner.name,
            winning_bid=float(winning_bid),
            clearing_price=float(clearing_price),
            revenue=float(revenue),
            efficiency=allocative_efficiency,
            winner_value=float(realised_values[highest]),
            runner_up_value=float(runner_up_value),
            winner_budget_remaining=float(winner.budget),
            notes=", ".join(notes) if notes else "",
        )
        results.append(result)

    return results


def summarise(results: list[AuctionResult]) -> dict:
    efficiency_rate = np.mean([r.efficiency for r in results])
    revenue_series = [r.revenue for r in results]
    winner_curse_count = sum("winner's curse" in r.notes for r in results)

    return {
        "rounds": len(results),
        "mean_revenue": float(np.mean(revenue_series)),
        "median_revenue": float(np.median(revenue_series)),
        "efficiency_rate": float(efficiency_rate),
        "winner_curse_frequency": winner_curse_count / len(results),
        "final_budgets": {r.winner: r.winner_budget_remaining for r in results[-3:]},
    }


def save_results(results: list[AuctionResult], output_path: Path) -> None:
    import csv

    fieldnames = list(asdict(results[0]).keys())
    with output_path.open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(asdict(result))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rounds", type=int, default=30, help="Number of auction rounds to simulate")
    parser.add_argument("--seed", type=int, default=206, help="Random seed for reproducibility")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("computational_scientist/results/auction_rounds.csv"),
        help="Where to save round-level results",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("computational_scientist/results/auction_summary.json"),
        help="Where to save summary statistics",
    )
    parser.add_argument(
        "--common-value-weight",
        type=float,
        default=0.25,
        help="Weight on the common-value component (0 = private values only)",
    )

    args = parser.parse_args()

    bidders = [
        BidderState(name="Rational", budget=18.0, strategy="rational_threshold"),
        BidderState(name="Optimist", budget=18.0, strategy="bounded_optimist"),
        BidderState(name="Conserver", budget=18.0, strategy="cautious_conserver"),
    ]

    results = run_simulation(
        num_rounds=args.rounds,
        bidders=[BidderState(**asdict(b)) for b in bidders],
        value_mean=np.log(6.0),
        value_sigma=0.45,
        common_value_weight=args.common_value_weight,
        seed=args.seed,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_results(results, args.output)

    summary = summarise(results)
    args.summary.write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
