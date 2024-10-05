from game1 import nok_question
from game2 import geometric_progression_question
from engine import run_game

def main():
    print("Choose a game:")
    print("1. 'LCM' Game")
    print("2. 'Geometric Progression' Game")

    choice = input("Enter the game number: ")

    if choice == "1":
        run_game(nok_question)
    elif choice == "2":
        run_game(geometric_progression_question)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
