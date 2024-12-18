import math
import re
from tkinter import Button, Tk, Entry

root = Tk()
root.title("calculatorр_tkinter")
root.geometry("300x400")


entry = Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

# button 1
button1 = Button(root, text="1", font=("Arial", 20),
                 command=lambda: entry.insert("end", "1"))
button1.grid(row=1, column=0, sticky="nsew")

# button 2
button2 = Button(root, text="2", font=("Arial", 20),
                 command=lambda: entry.insert("end", "2"))
button2.grid(row=1, column=1, sticky="nsew")

# button 3
button3 = Button(root, text="3", font=("Arial", 20),
                 command=lambda: entry.insert("end", "3"))
button3.grid(row=1, column=2, sticky="nsew")

# button 4
button4 = Button(root, text="4", font=("Arial", 20),
                 command=lambda: entry.insert("end", "4"))
button4.grid(row=2, column=0, sticky="nsew")

# button 5
button5 = Button(root, text="5", font=("Arial", 20),
                 command=lambda: entry.insert("end", "5"))
button5.grid(row=2, column=1, sticky="nsew")

# button 6
button6 = Button(root, text="6", font=("Arial", 20),
                 command=lambda: entry.insert("end", "6"))
button6.grid(row=2, column=2, sticky="nsew")

# button 7
button7 = Button(root, text="7", font=("Arial", 20),
                 command=lambda: entry.insert("end", "7"))
button7.grid(row=3, column=0, sticky="nsew")

# buuton 8
button8 = Button(root, text="8", font=("Arial", 20),
                 command=lambda: entry.insert("end", "8"))
button8.grid(row=3, column=1, sticky="nsew")

# button 9
button9 = Button(root, text="9", font=("Arial", 20),
                 command=lambda: entry.insert("end", "9"))
button9.grid(row=3, column=2, sticky="nsew")

# button 0
button0 = Button(root, text="0", font=("Arial", 20),
                 command=lambda: entry.insert("end", "0"))
button0.grid(row=4, column=1, sticky="nsew")

# button +
button_plus = Button(root, text="+", font=("Arial", 20),
                     command=lambda: entry.insert("end", "+"))
button_plus.grid(row=1, column=3, sticky="nsew")

# button -
button_minus = Button(root, text="-", font=("Arial", 20),
                      command=lambda: entry.insert("end", "-"))
button_minus.grid(row=2, column=3, sticky="nsew")

# button *
button_multiply = Button(root, text="*", font=("Arial", 20),
                         command=lambda: entry.insert("end", "*"))
button_multiply.grid(row=3, column=3, sticky="nsew")

# button /
button_divide = Button(root, text="/", font=("Arial", 20),
                       command=lambda: entry.insert("end", "/"))
button_divide.grid(row=4, column=3, sticky="nsew")

# button %
button_percent = Button(root, text="%", font=("Arial", 20),
                        command=lambda: entry.insert("end", "%"))
button_percent.grid(row=1, column=4, sticky="nsew")

# button C
button_clear = Button(root, text="C", font=("Arial", 20),
                      command=lambda: (clear_entry(), print("Нажать C")))
button_clear.grid(row=4, column=0, sticky="nsew")

# button √
# a module for working with the root

button_sqrt = Button(root, text="√", font=("Arial", 20),
                     command=lambda: calculate_sqrt())
button_sqrt.grid(row=2, column=4, sticky="nsew")

# button sin
button_sin = Button(root, text="sin", font=("Arial", 20),
                    command=lambda: calculate_trig("sin"))
button_sin.grid(row=3, column=4, sticky="nsew")

# button cos
button_cos = Button(root, text="cos", font=("Arial", 20),
                    command=lambda: calculate_trig("cos"))
button_cos.grid(row=4, column=4, sticky="nsew")


# rows and columns are being stretched
root.grid_rowconfigure(0, weight=0)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(5):
    root.grid_columnconfigure(j, weight=1)


def clear_entry():
    entry.delete(0, "end")


def calculate():
    try:
        expression = entry.get()
        # interest processing
        expression = re.sub(r"(\d+)\s*\+\s*(\d+)%",
                            r"(\1 + (\1 * \2 / 100))", expression)
        expression = re.sub(r"(\d+)\s*-\s*(\d+)%",
                            r"(\1 - (\1 * \2 / 100))", expression)

        expression = re.sub(r"(\d+)%", r"(\1 / 100)", expression)

        result = eval(expression)  # calculating the result

        if result.is_integer():  # convert to an integer
            result = int(result)

        entry.delete(0, "end")
        entry.insert("end", str(result))

    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Оmistake")


def calculate_sqrt():
    try:
        value = float(entry.get())
        if value < 0:
            raise ValueError(
                "It is impossible to calculate the root of a negative number")

        # Calculating the square root
        result = math.sqrt(value)

        # We clean and paste the result
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Mistake")


def calculate_trig(func):
    try:
        # Getting the value from the input field
        value = float(entry.get())

        # Converting the value
        radians = math.radians(value)

        # Calculating the result
        if func == "sin":
            result = math.sin(radians)
        elif func == "cos":
            result = math.cos(radians)

        # Clearing the field and showing the result
        entry.delete(0, "end")
        entry.insert("end", str(result))
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Mistake")


# buttun =
button_equal = Button(root, text="=", font=("Arial", 20),
                      command=calculate)
button_equal.grid(row=4, column=2, sticky="nsew")

root.mainloop()
