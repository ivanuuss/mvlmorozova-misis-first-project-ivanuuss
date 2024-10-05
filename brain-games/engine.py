def run_game(game_logic, max_rounds=3):
    """
    Общий движок для запуска игр.
    :param game_logic: Функция, которая возвращает (вопрос, правильный ответ)
    :param max_rounds: Количество раундов (по умолчанию 3)
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for round_num in range(max_rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
