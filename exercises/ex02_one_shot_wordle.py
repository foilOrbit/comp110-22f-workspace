"""This code creates a Wordle puzzle in which the user gets one guess."""

__author__ = "730548982"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# The variable "secret" is assigned to the secret word and "guess" is assigned to the user's guess.
# The index is assigned to the user's guess and the result is the output.
secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
index: int = 0
result: str = ""

# This loop tells the user to input another guess if the length of the guess doesn't match the secret's length.
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

# This loop tests if the letters in the guess match the letters of the secret word.
# If the letter and index match, a green box emoji is added to "result". 
while index < len(guess):
    if guess[index] == secret[index]:
        result = f"{result}{GREEN_BOX}"
    else:
        # If not, a a variable reports on whether the character exists in the word (initally set to false).
        # The variable "alt_index" keeps track of the secret's index in the loop.
        character_exists: bool = False
        alt_index: int = 0
        # The loop checks each index of the secret word against the current guess's index.
        while character_exists is False and alt_index < len(secret):
            if secret[alt_index] == guess[index]:
                character_exists = True
            else:
                alt_index = alt_index + 1
        # If the guess's character matches one of the secret's characters, a yellow box emoji is added to "result".
        # If not, a white box is printed.
        if character_exists is True:
            result = f"{result}{YELLOW_BOX}"
        else:
            result = f"{result}{WHITE_BOX}"
    index = index + 1

print(result)

# This loop prints a message based on whether or not the user's word matches the secret word.
if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")