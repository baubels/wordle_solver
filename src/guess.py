""" Access API, take a random guess, and visualize guess results.
"""

import requests


def guess_daily(guess_str):
    url = "https://wordle.votee.dev:8000/daily"
    response = requests.get(url, params={"guess": guess_str, "size": len(guess_str)})
    return response.text


def guess_random(guess_str, seed: int):
    url = "https://wordle.votee.dev:8000/random"
    response = requests.get(
        url, params={"guess": guess_str.lower(), "size": len(guess_str), "seed": seed}
    )
    return response.text


def guess_correct(response_text)->bool:
    if all([rd["result"] == "correct" for rd in response_text]):
        return True
    return False


def visualize_results(response_text):

    correct_letters = []
    correct_positions = {}
    incorrect_letters = []
    print("\nserver response: ")
    for i, response_dict in enumerate(response_text):
        if response_dict["result"] == "present":
            print(f"_", end="")
            correct_letters.append(response_dict["guess"])
        elif response_dict["result"] == "correct":
            print(f'{response_dict["guess"]}', end="")
            correct_positions[i] = response_dict["guess"]
        else:
            print("X", end="")
            incorrect_letters.append(response_dict["guess"])
    print()
    return correct_positions, correct_letters, incorrect_letters

# vr = visualize_results(eval(response.text))
# print(vr)
# print(guess_correct(eval(guess_random('wreak', 129))))
# response_text = guess_random('wreax', 129)
# vr = visualize_results(eval(response_text))
# print(vr)
