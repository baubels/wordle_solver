
## Wordle Solver

Simple Wordle Solver. Filters guesses based off a dictionary of possible words and guess responses.

The strategy starts with an initial guess, and according to the API response
successively improves upon the previous guess until either the guess is correct
or until there are no available words that fit the solution*.

The iterations work as follows:

1. The API response tells you:
    - **a)** which characters don't exist in the solution  
    - **b)** which characters exist in the solution  
    - **c)** the exact positions of each correctly guessed character in the solution  

    This information is then stored in three objects that grow as the number of guesses increases.  

2. These objects filter a list of all possible words the solution may be.  
Words that are already guessed are further removed from this list.  

3. This filtered list is used to create a next-best guess. This guess is made with the following strategies:
    - **a)** Use all the remaining possible words, and determine the most likely characters that the incorrectly guessed characters may be. This next word is constructed in order of the most likely characters.  
    It is not usually a word, but is instead used to remove the number of possible words from the next call's response.  

    This guess is always going to decrease the size of possible words since it's constructed purely from characters not yet guessed.  
    - **b)** Once the filtered list is below a certain count, guess a word randomly from this list of possible words.  

4. If the number of possible words left is 1, this becomes the final guess.  
A final API call is then made to confirm if the guess is the solution.  

#### Usage

To use, run

```python3
python -m src.strategy
```

alternatively, use either the `apply_strategy_random`, `apply_strategy_daily` functions in `src/strategy`. For example, the run the daily challenge using an initial guess `guess`:

```python3
import src.strategy
src.strategy.apply_strategy_daily("guess")
```

and you will get information shown by the solver as it guesses until it reaches a solution.

