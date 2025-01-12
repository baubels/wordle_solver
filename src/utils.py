import copy


def fetch_all_words() -> list[str]:
    with open("all_words.txt", "r") as f:
        all_words = [line.strip().lower() for line in f if line.strip().lower().isalpha()]
    return all_words


def remaining_words(
    all_words, right_position: dict, has_chars: list[str], doesnt_have_chars: list[str], word_length:int
):
    filtered_words = []
    # filter words without wrong chars
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

    # filter words with exact position characters
    filtered_words_3 = []
    for word in filtered_words_2:
        if all([word[pos] == char for pos, char in right_position.items()]):
            filtered_words_3.append(word)
    return filtered_words_3


def top_contenders(remaining_poss: list[str], right_position: dict):
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
