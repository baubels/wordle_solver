
import random
from .guess import guess_correct, guess_daily, guess_random, visualize_results
from .utils import fetch_all_words, remaining_words, top_contenders

# strategy:
# 1. initial guess
# 2. filter for remaining words
# 3. get most likely remaining characters
# 4. guess with those characters
# 5. repeat steps 2 to 4 until success


def take_guess(guess_str: str, seed=42):
    all_words = fetch_all_words()
    all_correct_positions = {}
    all_correct_letters = []
    all_incorrect_letters = []

    # initial guess
    guess_made = eval(guess_random(guess_str, seed))

    i = 0
    old_remwords = []
    wrong_words = []
    while not guess_correct(guess_made):
        wrong_words.append(guess_str)

        print("-" * 50)
        print(f"\nguessing: {guess_str}")
        print(f"guess response: \n{guess_made}")
        # get remaining possible words
        correct_positions, correct_letters, incorrect_letters = visualize_results(
            guess_made
        )
        all_correct_positions.update(correct_positions)
        all_correct_letters.extend(correct_letters)
        all_incorrect_letters.extend(incorrect_letters)
        remwords = remaining_words(
            all_words, all_correct_positions, all_correct_letters, all_incorrect_letters, len(guess_str)
        )
        remwords = [item for item in remwords if item not in wrong_words]

        print(f"\ncorrect letters: {set(all_correct_letters)}")
        print(f"incorrect leters: {set(all_incorrect_letters)}\n")
        print(f"number of remaining possible words: {len(remwords)}")
        top_c = top_contenders(remwords, correct_positions)
        top_c = dict(sorted(top_c.items(), key=lambda item: item[1], reverse=True))
        print(remwords, top_c)

        # determine the next best guess
        # next best guess will be just a new set of characters using exclusively the top 5 remaining letters in top_c
        # this will happen until the number of remaining possible words is < 5
        i += 1
        if len(remwords) == 1:
            print(f"Only remaining possibility: {remwords[0]}")
            guess_str = remwords[0]
            if not guess_correct(eval(guess_random(guess_str, seed))):
                print(f"Correct answer not contained in the dictionary. Woops.")
                break
            else:
                break

        if (len(remwords) == 0) or (len(remwords) == len(old_remwords)):
            print("Daily word is not in the worldle dictionary! Quitting")
            break

        if len(remwords) < 5:
            guess_str = random.choice(remwords)
        else:
            old_guess_str_len = len(guess_str)
            guess_str = "".join(list(top_c)[: min(len(guess_str), len(top_c))])
            if len(guess_str) != old_guess_str_len:
                guess_str = guess_str + "a" * (old_guess_str_len - len(guess_str))

        guess_made = eval(guess_random(guess_str, seed))
        old_remwords = remwords

    was_guess_correct = guess_correct(eval(guess_random(guess_str, seed)))
    print(f"\nGuessing: '{guess_str}' ({was_guess_correct}) in {i+1} tries\n")
    return i + 1, was_guess_correct

# take_guess('youthfulness', seed=random.randint(1,1e5))
