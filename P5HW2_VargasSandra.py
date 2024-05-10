# Sandra Vargas
# May 6, 2024
# P5HW - MathQuiz
# This program is a menu-driven math quiz that allows the user to choose between addition, subtraction, or exiting the program.

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def addition_quiz():
    num1, num2 = generate_numbers()
    print("Adding Random Numbers")
    print(num1, "+", num2)
    correct_answer = num1 + num2
    return correct_answer

def subtraction_quiz():
    num1, num2 = generate_numbers()
    print("Subtracting Random Numbers")
    print(num1, "-", num2)
    correct_answer = num1 - num2
    return correct_answer

def main_menu():
    print("\nWelcome to Math Quiz")
    print("MAIN MENU")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            correct_answer = addition_quiz()
        elif choice == '2':
            correct_answer = subtraction_quiz()
        elif choice == '3':
            print("Thank you for playing!")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please choose one of the menu options.")
            continue

        num_guesses = 0
        while True:
            user_answer = int(input("Enter your answer: "))
            num_guesses += 1
            if user_answer == correct_answer:
                print("Congratulations! Your answer is correct.")
                print("Number of guesses:", num_guesses)
                break
            else:
                if user_answer < correct_answer:
                    print("Sorry, guess is too low. Try again.")
                else:
                    print("Sorry, guess is too high. Try again.")

if __name__ == "__main__":
    main()
