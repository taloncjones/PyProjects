# File: CodeSnippets.py
# Use: This file will contain useful code snippets that may be needed in the future
# Author: Talon Jones

# Purpose: Reduce the amount of re-written code


def getYesNo(question: str):
    # Gets user input to <question: str> in y/yes/n/no form and returns True or False.
    y_n = ''
    while True:
        y_n = input(question).lower()
        if y_n in {'y', 'yes'}:
            return True
        elif y_n in {'n', 'no'}:
            return False
        else:
            print('Invalid option. Please enter y/n.')