
"""Validate the strategy.

The strategy is validated by:
    1) guessing a large number of times on a set of words from lengths a to b.
    2) producing metrics and plots indicating guess statistics and success rate.
"""

import random
import statistics
import os

import matplotlib.pyplot as plt
import numpy as np

from src.strategy import apply_strategy

# run strategy
for i in range(3, 13):
    n_runs      = 30
    n_takes     = []
    correct     = []
    init_guess  = "abcdefghijklmnopqrstuv"[:i]
    for _ in range(n_runs):
        n_gs, wgc = apply_strategy(init_guess, seed=random.randint(1, 1e5))
        n_takes.append(n_gs)
        correct.append(wgc)
    n_takes = np.array(n_takes)
    correct = np.array(correct)

    # save experiment data
    mean = statistics.mean(n_takes[correct])
    medi = statistics.median(n_takes[correct])
    stds = np.std(n_takes[correct])
    winrate = np.mean(correct[n_takes <= 6])


    plt.hist(n_takes[correct], bins=5)

    os.makedirs(f"./val/letters_{len(init_guess)}/", exist_ok=True)
    plt.savefig(f"./val/letters_{len(init_guess)}/average_guesses_to_success.png")
    plt.close()

    with open(f"./val/letters_{len(init_guess)}/strategy_statistics.txt", "w") as f:
        f.write(f"mean n guesses {mean}\n")
        f.write(f"median n guesses {medi}\n")
        f.write(f"std of guess {stds}\n")
        f.write(f"winrate {winrate}\n")
