from tkinter import *
from tkinter import messagebox

# name of program #
convert = Tk()

# Sets size and title
convert.title("IDEAL BODY MASS INDEX CALCULATOR")
convert.geometry("700x600")
convert.config(bg="#32a895")

def activate(value):
    variable.set(value)
    if value != "Select...":
        age_entry.config(state='normal')
    else:
        age_entry.config(state='readonly')

# With user inputs calculate BMI
def bmi_calc():
    try:
        float(weight_entry.get())
        float(height_entry.get())
        float(age_entry.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + 11.5
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        elif variable.get() == "Female":
            result = ((0.5 * float(weight_entry.get())) / ((float(height_entry.get()) / 100) ** 2)) + (
                        0.03 * float(age_entry.get())) + 11
            result = round(result, 1)
            ideal_field.config(state='normal')
            ideal_field.insert(0, result)
            ideal_field.config(state='readonly')
            result_bmi = float(weight_entry.get()) / ((float(height_entry.get()) / 100) ** 2)
            bmi_field.config(state='normal')
            bmi_field.insert(0, round(result_bmi, 1))
            bmi_field.config(state='readonly')
        if result_bmi < 18.5:
            category.config(text='Underweight')
        elif 18.5 <= result_bmi < 25:
            category.config(text='Normal weight')
        elif 25 <= result_bmi < 30:
            category.config(text='Overweight')
        elif result_bmi >= 30:
            category.config(text='Obese')

    except ValueError:
        messagebox.showerror(title=None, message='Gender not specified')
        delete()


def delete():
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    age_entry.config(state='normal')
    bmi_field.config(state='normal')
    ideal_field.config(state='normal')
    age_entry.delete(0, END)
    bmi_field.delete(0, END)
    ideal_field.delete(0, END)
    age_entry.config(state='readonly')
    bmi_field.config(state='readonly')
    ideal_field.config(state='readonly')
    weight_entry.focus()
    variable.set(options[0])

# Creating Labels #
header = Label(convert, text='Body Mass Index', fg='black')
frame = Frame(convert, width=500, height=200, relief='raised')
weight = Label(frame, text="Weight in kg:", fg='black')
height = Label(frame, text="Height in cm:", fg='black')
gender = Label(frame, text="Gender:", fg='black')
age = Label(frame, text="Age:", fg='black')
bmi = Label(convert, text="BMI:", fg="black")
ideal_bmi = Label(convert, text='Ideal BMI:', fg="black")
category_head = Label(convert, text="Category:", fg='black')


# Creating Entries #
weight_entry = Entry(frame)
height_entry = Entry(frame)
age_entry = Entry(frame, state='readonly')
bmi_field = Entry(convert, state='readonly')
ideal_field = Entry(convert, state='readonly')
category = Label(convert, width=20, fg='black')

# Creating Butttons #
clear = Button(convert, text='Clear', command=delete)
quit = Button(convert, text='Exit', command='exit')
calculate = Button(convert, text="Calculate your Ideal Body Mass Index", width=50, command=bmi_calc)

# Creating Dropdown #
options = ['Select...', 'Male', "Female"]
variable = StringVar(frame)
variable.set(options[0])

gender_menu = OptionMenu(frame, variable, *options, command=activate)

# Placing Labels #
header.place(x=280, y=20)
frame.place(x=100, y=50)
weight.place(x=100, y=20)
height.place(x=100, y=62)
gender.place(x=100, y=105)
age.place(x=100, y=160)
calculate.place(x=170, y=280)
bmi.place(x=100, y=331)
ideal_bmi.place(x=375, y=331)
category_head.place(x=320, y=380)
clear.place(x=285, y=480)
quit.place(x=380, y=480)

# Placing Entries #
weight_entry.place(x=200, y=20)
age_entry.place(x=200, y=160)
height_entry.place(x=200, y=62)
bmi_field.place(x=150, y=331)
ideal_field.place(x=450, y=331)
category.place(x=275, y=415)
gender_menu.place(x=200, y=105)

# Keeps the program running
convert.mainloop()
