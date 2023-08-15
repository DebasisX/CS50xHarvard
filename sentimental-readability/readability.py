import math
from cs50 import get_string


def calculate_grade(text):  # function to generate grade
    letters = 0.0
    words = 1.0  # adding a word for the last word
    sentences = 0.0
    list = ['?', '.', '!']
    for t in text:  # checking each charater in string
        if t == ' ':
            words += 1
        elif t in list:  # checking for ?, ., !
            sentences += 1
        elif t.isalpha():  # checking if it's a letter
            letters += 1
    S = (sentences / words) * 100
    L = (letters / words) * 100
    grade = (0.0588 * L) - (0.296 * S) - 15.8  # using Coleman-Liau index
    grade = round(grade)
    return grade


text = get_string("Text: ")
grade = calculate_grade(text)
if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")