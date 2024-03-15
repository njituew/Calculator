from tkinter import *


def make_digit_button(window, calc, digit):
    return Button(window, text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(window, calc, digit))


def make_operation_button(window, calc, operation):
    return Button(window, text=operation, bd=5, font=('Arial', 13), fg='red',
                  command=lambda: add_operation(window, calc, operation))


def add_digit(window, calc, digit):
    if calc.get() == '0' and digit != '.':
        calc.delete(0, END)
    calc.insert('end', digit)


def add_operation(window, calc, operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value + operation)
