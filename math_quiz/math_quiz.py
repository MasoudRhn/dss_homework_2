import random


def Random_int(min, max):
    """
    This function generates a random integer between min and max.
    """
    return random.randint(min, max)


def Random_operator():
    """ "
    This function generates a random operator.
    """

    return random.choice(["+", "-", "*"])


def Operation(n1, n2, o):
    """ "
    This function generates a math problem.
    """
    p = f"{n1} {o} {n2}"
    if o == "+":
        a = n1 + n2
    elif o == "-":
        a = n1 - n2
    elif o == "*":
        a = n1 * n2
    return p, a


def math_quiz():
    score = 0
    num_questions = 4
    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems, and you need to provide the correct answers."
    )

    for _ in range(num_questions):
        n1 = Random_int(1, 10)
        n2 = Random_int(1, 5)
        o = Random_operator()

        PROBLEM, ANSWER = Operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric answer.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{num_questions}")


if __name__ == "__main__":
    math_quiz()
