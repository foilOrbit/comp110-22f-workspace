"""This program creates a number guessing game."""
__author__ = "730548982"

# This determines the python monster's hitpoints
# It is the global points variable
points: int = 50
# This determines the player's health
health: int = 30
player: str = ""
PYTHON: str = "\U0001F40D"
# Four emojis used: scared face, python, congratulations, and gravestone
NAMED_CONSTANT: str = "\U00000000 \U00000000 \U00000000 \U00000000"


def main() -> None:
    """This is the main function that calls other parts of the program."""  
    global player
    global points
    global health
    greet()
    print(f"We're so grateful you've come to our aid {player}.")
    # This starts the game loop. The variable "options" determines if the player attacks, heals, or quits
    print("Would you like to attack with sword, request divine intervention, or end the game?")
    options: str = input("Enter 1 for sword, 2 for divine intervention, and 3 to end the game: ")
    # This makes sure the player has the right input
    while len(options) != 1 or options != "1" and options != "2" and options != "3":
        options = input("Only the number 1, 2, or 3 can be inputted. Please try again: ")
    while options != "3":
        if options == "1":
            attack()  
        else:
            divine_dmg: int = divine_intervention(points)
            if divine_dmg == 0:
                print("Sorry, the stars did not align! No damage dealt.")
            else:
                print(f"Nice! The heavens smote {PYTHON}! 10 damage dealt. {PYTHON} has {points} health remaining.")
        python_attack()
        options = input("Enter 1 for attack, 2 for divine intervention, and 3 to end the game: ") 
        while len(options) != 1 or options != "1" and options != "2" and options != "3":
            options = input("Only the number 1, 2, or 3 can be inputted. Please try again: ")
    end_game()
       

def greet() -> None:
    """This function greets the player and prompts them to input their name."""
    global player
    print(f"\U0001F628 CRIKEY! The perilous {PYTHON} has appeared! \U0001F628")
    player = input("Thank goodness a great hero like you has come to save us. Please, tell me your name: ")


def attack() -> None:
    """This function makes the player choose a weapon to attack with."""
    global points
    print(f"What is your command, {player}?")
    decide: str = input("Enter 1 to strike with sword and 2 to shoot with bow: ")
    while len(decide) != 1 or decide != "1" and decide != "2":
        decide = input("Only the number 1 or 2 can be entered. Please try again: ")
    if decide == "1":
        attack: int = sword()
    else:
        attack: int = bow()
    points -= attack
    if points <= 0:
        print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
        print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
        print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
        exit()
    print(f"Nice! You did {attack} damage. {PYTHON} has {points} health remaining.")


def sword() -> int:
    """This function attacks the python with the sword. Attacks always do 5 damage."""
    return 5


def bow() -> int:
    """This function attacks the python with the bow. Attacks do 3-8 damage."""
    from random import randint
    return randint(3, 8)


# def heal(hitpoints: int) -> int:
#     """This function heals the player for a random integer from 5-10 if the player guesses the right number."""
#     from random import randint
#     global health
#     predict: str = input(f"{player}, guess the magic number (either 1 or 2) right to heal: ")
#     while predict != "1" and predict != "2" and len(predict) != 1:
#         predict = input("Only the number 1 or 2 can be entered. Please try again: ")
#     wish: int = randint(1, 2)
#     if wish == int(predict):
#         heal: int = randint(3, 8)
#         return heal
#     else:
#         return 0
    
def divine_intervention(py_hp: int) -> int:
    """This function damages the python for 10 hitpoints if the player guesses the right number."""
    from random import randint
    global points
    predict: str = input(f"{player}, roll the cosmic dice (pick a # from 1-6): ")
    while len(predict) != 1 or int(predict) < 1 or int(predict) > 6:         
        predict = input("Only a number from 1-6 can be entered. Please try again: ")
    dice: int = randint(1, 6)
    if dice == int(predict):
        py_hp -= 10
        points = py_hp
        return 10
        if points <= 0:
            print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
            print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
            print(f" \U0001f389 Congratulations! \U0001f389 You killed {PYTHON}!")
            exit()
    else:
        return 0


def end_game() -> None:
    """This function ends the game before the python is dead."""
    print("Thanks for playing!")
    print(f"{PYTHON} had {points} health remaining.")
    exit()


def python_attack() -> int:
    """This function calculates and outputs the damage the python does to the player each turn. Python has 80% accuracy."""
    global health
    from random import randint
    strike: int = randint(1, 5)
    if strike == 1:
        print("Woohoo! The python's attack missed.") 
    else:
        health -= strike
        if health <= 0:
            print(f"Oh nooooooo! {PYTHON} has vanquished you! \U0001FAA6 \U0001FAA6 \U0001FAA6  Better luck next time!")
            exit()
        print(f"{PYTHON} did {strike} damage. You have {health} health remaining.")
        

if __name__ == "__main__":
    main()
