
import copy

def fetch_all_words() -> list[str]:
    """
    Fetch all the words from the word dictionary. Return words as a list[str] of words.
    """
    with open("./data/all_words.txt", "r") as f:
        all_words = [line.strip().lower() for line in f if line.strip().lower().isalpha()]
    return all_words


def remaining_words(
    all_words:list[str], right_position: dict, has_chars: list[str], doesnt_have_chars: list[str], word_length:int
)->list[str]:
    """
    Considering a list of words, return a new list of words that satisfies inclusion/exclusion criteria.

    params:
        all_words [list]:       a list of strings, each representing one word
        right_position [dict]:  a dictionary with int keys and char values
                                the keys represents an index character of a string
                                the values represents what character can be expected at that index
        has_chars [list[str]]:  a list of characters denoting which characters appear in the solution.
        doesnt_have_chars [list[str]]: a list of characters denoting which characters don't appear in the solution
        word_length [int]:      an integer specifying the length of the solution word.
    """
    # filter words without wrong chars
    filtered_words = []
    for word in all_words:
        if len(word) == word_length:
            chars_in_word = [char in word for char in doesnt_have_chars]
            if not any(chars_in_word):
                filtered_words.append(word)

    # filter words with said chars
    filtered_words_2 = []
    for word in filtered_words:
        chars_in_word = [char in word for char in has_chars]
        if all(chars_in_word):
            filtered_words_2.append(word)

    # filter words with chars in their exact positions
    filtered_words_3 = []
    for word in filtered_words_2:
        if all([word[pos] == char for pos, char in right_position.items()]):
            filtered_words_3.append(word)
    return filtered_words_3


def top_contenders(remaining_poss: list[str], right_position: dict)->dict:
    """
    Given a list of possible remaining words and a dictionary of known characters at specific indices, 
    {index: character}, return a dictionary that counts the number of occurences of 
    characters across all remaining possible words for character locations not already known.
    """
    remaining_letters = {}
    for word in remaining_poss:
        for i in range(len(word)):
            if i not in right_position:
                if word[i] in remaining_letters:
                    remaining_letters[word[i]] += 1
                else:
                    remaining_letters[word[i]] = 1
    return remaining_letters


# all_words       = fetch_all_words()
# remwords        = remaining_words(all_words, {0:'a', 4:'e'}, ['a', 'e'], ['b', 'c', 'd'])
# top_c           = top_contenders(remwords, {0:'a', 4:'e'})
# top_c           = dict(sorted(top_c.items(), key=lambda item: item[1], reverse=True))
# print(top_c)
