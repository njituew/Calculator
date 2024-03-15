from tkinter import *
from config import *


def calculate():
    value = calc.get()
    calc.delete(0, END)
    calc.insert('end', eval(value))


def c_operation():
    calc.delete(0, END)
    calc.insert('end', 0)


window = Tk()
window.title('Calculator')
window.geometry('240x330')
window['bg'] = 'LightBlue'

window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)
window.grid_rowconfigure(5, minsize=60)

calc = Entry(window, justify=RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(column=0, row=0, columnspan=4, stick='we', padx=3, pady=3)

make_digit_button(window, calc, '7').grid(column=0, row=1, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '8').grid(column=1, row=1, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '9').grid(column=2, row=1, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '4').grid(column=0, row=2, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '5').grid(column=1, row=2, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '6').grid(column=2, row=2, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '1').grid(column=0, row=3, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '2').grid(column=1, row=3, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '3').grid(column=2, row=3, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '.').grid(column=0, row=4, stick='wens', padx=3, pady=3)
make_digit_button(window, calc, '0').grid(column=1, row=4, stick='wens', padx=3, pady=3)

make_operation_button(window, calc, '+').grid(column=3, row=1, stick='wens', padx=3, pady=3)
make_operation_button(window, calc, '-').grid(column=3, row=2, stick='wens', padx=3, pady=3)
make_operation_button(window, calc, '*').grid(column=3, row=3, stick='wens', padx=3, pady=3)
make_operation_button(window, calc, '/').grid(column=2, row=4, stick='wens', padx=3, pady=3)

Button(window, text='=', bd=5, font=('Arial', 13), fg='blue', command=calculate).grid(column=3, row=4, stick='wens',
                                                                                      padx=3, pady=3)
Button(window, text='C', bd=5, font=('Arial', 13), fg='blue', command=c_operation).grid(column=0, row=5, stick='wens',
                                                                                       padx=3, pady=3)

Label(window, text='njituew', bg='LightBlue').grid(column=1, row=5, columnspan=3, stick='we')

window.mainloop()
