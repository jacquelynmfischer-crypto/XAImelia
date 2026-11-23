"""Reproduce the XAImelia survey results from the Google Sheet export.

Usage:
    python analysis/analyze.py responses.csv [--exclude-id ID ...]

Export the "AImelia Survey Responses" sheet as CSV (File > Download > CSV).
Columns: timestamp, id, name, age, ai, pre, post, minutes, message.
Ratings are scored 0 (None) to 4 (Expert). Names are never printed.
Requires pandas and scipy.
"""
import argparse, json
import numpy as np
import pandas as pd
from scipy import stats

UNITS = ["Interpretable ML", "Explainable ML", "Mechanistic Interpretability",
         "Adversarial AI", "Alignment", "Transparent AI"]
AI = ["None", "Beginner", "Competent", "Proficient", "Expert"]

def parse(x):
    try:
        v = json.loads(x)
        return v if isinstance(v, list) and len(v) == 6 else None
    except (TypeError, ValueError):
        return None

def summarize(df, label):
    P = np.array(df.pre.tolist(), float); Q = np.array(df.post.tolist(), float)
    a, b = P.mean(1), Q.mean(1); g = b - a
    print(f"\n== {label} (n = {len(df)}) ==")
    print(f"Familiarity before {a.mean():.2f}, after {b.mean():.2f}, gain {g.mean():+.2f} per unit "
          f"({6 * g.mean():+.1f} total)")
    print(f"Improved {int((g > 0).sum())}, no change {int((g == 0).sum())}, decreased {int((g < 0).sum())}")
    if len(df) > 1 and g.std(ddof=1) > 0:
        w = stats.wilcoxon(b, a, alternative="greater")
        print(f"Wilcoxon signed-rank (one-sided): W = {w.statistic:.0f}, p = {w.pvalue:.4f}; "
              f"effect size d_z = {g.mean() / g.std(ddof=1):.2f}")
    for u, name in enumerate(UNITS):
        p = stats.wilcoxon(Q[:, u], P[:, u], alternative="greater").pvalue if (Q[:, u] != P[:, u]).any() else float("nan")
        print(f"  Unit {u + 1} {name:<29} {P[:, u].mean():.2f} -> {Q[:, u].mean():.2f}   p = {p:.4f}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("--exclude-id", nargs="*", default=[])
    args = ap.parse_args()
    df = pd.read_csv(args.csv)
    df = df[~df.id.isin(args.exclude_id)].drop_duplicates("id", keep="last")
    df["pre"] = df.pre.map(parse); df["post"] = df.post.map(parse)
    started = df[df.pre.notna()]
    done = started[started.post.notna()].copy()
    print(f"Started {len(started)}, finished {len(done)} ({len(done) / max(1, len(started)):.0%} completion)")
    print(f"Ages {started.age.min()} to {started.age.max()}, median {started.age.median():.0f}")
    print(f"AI familiarity before playing: mean {started.ai.mean():.2f} of 4")
    pre_all = np.array(started.pre.tolist(), float)
    zero = (pre_all.sum(1) == 0)
    print(f"Rated every XAI concept None before playing: {int(zero.sum())} of {len(started)} "
          f"({int((zero & (started.ai.values >= 2)).sum())} of them Competent or higher with AI); "
          f"mean XAI familiarity {pre_all.mean():.2f} of 4")
    print(f"Median minutes played: {pd.to_numeric(done.minutes, errors='coerce').median():.0f}")
    summarize(done, "All players who finished")
    varied = done[done.post.map(lambda v: len(set(v)) > 1)]
    print(f"\nPlayers who gave every unit the same post-game rating: {len(done) - len(varied)} of {len(done)}")
    if len(varied) > 1:
        summarize(varied, "Sensitivity check: players whose post-game ratings varied by unit")
    print("\nGain by AI familiarity:")
    done["gain"] = [np.mean(q) - np.mean(p) for p, q in zip(done.pre, done.post)]
    for k, grp in done.groupby("ai"):
        print(f"  {AI[int(k)]:<11} n = {len(grp)}  gain {grp.gain.mean():+.2f} per unit")

if __name__ == "__main__":
    main()
