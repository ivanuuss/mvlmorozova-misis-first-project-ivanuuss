import random
from engine import run_game


def generate_progression(length, start, step):
    return [start * (step ** i) for i in range(length)]


def geometric_progression_question():
    progression_length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(2, 5)
    progression = generate_progression(progression_length, start, step)

    missing_index = random.randint(0, progression_length - 1)
    correct_answer = progression[missing_index]

    progression[missing_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


if __name__ == "__main__":
    run_game(geometric_progression_question)
