"""
Simulates a hiring process for n candidates.

Uses the optimal rule: reject first  n/e candidates, then pick the next better-than-seen.

Repeats this over many trials.

Computes the proportion of times the best candidate was selected.

Intuition
Rejecting the first ∼ 37%
∼37% lets you calibrate: you get a sense of how good the candidates are.

Then you use this information to act when someone better comes along.

It balances exploration (learning) and exploitation (choosing).
"""

import random

def candidate_selection_problem(n=100, trials=10000):
    """
    Simulates the candidate selection problem.

    Parameters:
        n: number of candidates
        trials: number of simulation runs

    Returns:
        Estimated probability of selecting the best candidate.
    """
    success_count = 0
    cutoff = int(n / 2.71828)  # Optimal stopping index ≈ n/e

    for _ in range(trials):
        candidates = list(range(1, n + 1))  # Candidate qualities (1 = worst, n = best)
        random.shuffle(candidates)         # Random interview order
        best_seen = max(candidates[:cutoff])

        for i in range(cutoff, n):
            if candidates[i] > best_seen:
                # Choose this candidate
                if candidates[i] == n:     # Is it the best overall?
                    success_count += 1
                break
        else:
            # If we never picked anyone, check if last one is the best
            if candidates[-1] == n:
                success_count += 1

    return success_count / trials

# Example usage
prob = candidate_selection_problem(n=100, trials=10000)
print(f"Estimated success probability: {prob:.4f}")
