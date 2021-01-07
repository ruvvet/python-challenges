# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    method = input('Pick one: +, -, *, /:  ')
    numbers = input('input 2 numbers separated by a ,:  ')
    a, b = map(lambda x: int(x), numbers.split(','))

    if method == '+':
        return a+b
    elif method == '-':
        return a-b
    elif method == '*':
        return a*b
    elif method == '/':
        return a//b


print(calculator())
