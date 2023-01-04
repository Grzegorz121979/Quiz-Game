"""
Quiz Game
"""
questions = ("How far is from the earth to the moon?: ", "The capital of Australia?: ")

options = (("A. 102200", "B. 855300", "C. 384400"), ("A. Canberra", "B. Sydney", "C. Wellington"))

answers = ("C", "A")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C): ").upper()
    question_num += 1
    if guess == answers[question_num]:
        print("Correct")
    else:
        print(f"The answer is {option[question_num]}")
