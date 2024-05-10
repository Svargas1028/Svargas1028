# Sandra Vargas
# May 6, 2024
# P5HW - MathQuiz
# This program generates random math problems (addition, subtraction) for the user to solve.

import random

def generate_problem():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operation = random.choice(['+', '-'])
    return num1, num2, operation

def check_answer(num1, num2, operation, answer):
    if operation == '+':
        return answer == num1 + num2
    elif operation == '-':
        return answer == num1 - num2

def main():
    num_guesses = 0
    num1, num2, operation = generate_problem()
    print(num1, operation, num2)
    while True:
        user_answer = int(input("Enter your answer: "))
        num_guesses += 1
        if check_answer(num1, num2, operation, user_answer):
            print("Congratulations! You got the correct answer in", num_guesses, "guesses.")
            break
        else:
            if operation == '+':
                if user_answer < num1 + num2:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
            elif operation == '-':
                if user_answer < num1 - num2:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")

if __name__ == "__main__":
    main()
