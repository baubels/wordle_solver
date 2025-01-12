
# validate the chosen strategy
# output statistics on average win-rate

import random
import statistics
import os

import matplotlib.pyplot as plt
import numpy as np

from src.strategy import take_guess

# run strategy
for i in range(5, 13):
    n_runs      = 30
    n_takes     = []
    correct     = []
    init_guess  = "abcdefghijklmnopqrstuv"[:i]
    for _ in range(n_runs):
        n_gs, wgc = take_guess(init_guess, seed=random.randint(1, 1e5))
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
