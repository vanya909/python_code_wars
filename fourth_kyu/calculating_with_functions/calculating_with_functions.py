'''
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division.

vanya_909
'''


def zero(operation = ''):
    return 0 if operation == '' else eval('0 ' + operation)

def one(operation = ''):
    return 1 if operation == '' else eval('1 ' + operation)

def two(operation = ''):
    return 2 if operation == '' else eval('2 ' + operation)

def three(operation = ''):
    return 3 if operation == '' else eval('3 ' + operation)

def four(operation = ''):
    return 4 if operation == '' else eval('4 ' + operation)

def five(operation = ''):
    return 5 if operation == '' else eval('5 ' + operation)

def six(operation = ''):
    return 6 if operation == '' else eval('6 ' + operation)

def seven(operation = ''):
    return 7 if operation == '' else eval('7 ' + operation)

def eight(operation = ''):
    return 8 if operation == '' else eval('8 ' + operation)

def nine(operation = ''):
    return 9 if operation == '' else eval('9 ' + operation)


def plus(operand):
    return f'+ {operand}'

def minus(operand):
    return f'- {operand}'

def times(operand):
    return f'* {operand}'

def divided_by(operand):
    return f'// {operand}'