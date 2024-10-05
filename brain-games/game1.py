import math
import random
from engine import run_game


def find_nok(a, b):
    return abs(a * b) // math.gcd(a, b)


def nok_of_three_numbers(x, y, z):
    return find_nok(find_nok(x, y), z)


def nok_question():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = nok_of_three_numbers(*numbers)
    return question, correct_answer


if __name__ == "__main__":
    run_game(nok_question)
