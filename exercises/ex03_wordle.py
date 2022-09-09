"""This code creates a fully functional Wordle puzzle."""

__author__ = "730548982"


def contains_char(searched: str, searched_for: str) -> bool:
    """This function searches a word for a specific character."""
    assert len(searched_for) == 1
    i: int = 0
    exists: bool = False
    # This loop checks each letter of the secret word against one letter of the guess word and outputs "True" if a match is found
    while i < len(searched):
        if searched[i] == searched_for:
            exists = True
            return exists
        else:
            i += 1
    return exists


def emojified(guess: str, secret: str) -> str:
    """This function takes a guess word and verifies if each letter matches up with a secret word using the contains_char function."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    i: int = 0
    # This loop outputs a green box for every guess letter with matching position and value in the secret word, 
    # a yellow box for every letter with a matching value but not postion in the secret word,
    # and a white box for every letter not present in the word.
    while i < len(secret):   
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            result += YELLOW_BOX   
        else:
            result += WHITE_BOX
        i += 1
    return result 


def input_guess(expected_length: int) -> str:
    """This function verifies that a guess is a set length and prompts the user if that condition isn't met."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ") 
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    win: bool = False
    turn: int = 1
    # This loop runs the game. It counts turns, notifies the user of the current turn, and verifies guesses.
    # It takes the guess from input_guess and checks it against the secret word using emojified.
    while win is False and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        # If the guess is true, the user gets a win message, and if not, the game ends and a loss message appears.
        if guess == secret:
            win = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if win is False and turn >= 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
    