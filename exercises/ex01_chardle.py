"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730548982"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

count: int = 0

print("Searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
    count = count + 1
if character == word[1]:
    print(character + " found at index 1")
    count = count + 1
if character == word[2]:
    print(character + " found at index 2")
    count = count + 1
if character == word[3]:
    print(character + " found at index 3")
    count = count + 1
if character == word[4]:
    print(character + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + character + " found in " + word)
if count == 1:
    print("1 instance of " + character + " found in " + word)
else:
    print(str(count) + " instances of " + character + " found in " + word)