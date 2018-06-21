# Calculator Application
# import gui tkinter
from tkinter import *
from tkinter import ttk

# creat calculator class
class Calculator:

    # store the value in current entry point
    calc_value = 0.0

    # way to track last math button
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    # get the current value in our entry
    def button_press(self, value):

        entry_val = self.number_entry.get()

        entry_val += value

        self.number_entry.delete(0, "end")

        self.number_entry.insert(0, entry_val)

    def isfloat(self, str_val):
        try:
            float(str_val)

            return True
        except ValueError:
            return False

    # logic when math button pressed
    def math_button_press(self, value):

        if self.isfloat(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            self.calc_value = float(self.entry_value.get())

            if value == "/":
                self.div_trigger = True
            elif value == "*":
                self.mult_trigger = True
            elif value == "+":
                self.add_trigger = True
            elif value == "-":
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    # equal button
    def equal_button_press(self):

        if self.add_trigger or self. sub_trigger or self.mult_trigger or self.div_trigger:

            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())


            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    # need root to work with interface
    def __init__(self, root):

        # string value to store
        self.entry_value = StringVar(root, value="")

        # title for calc
        root.title("Calculator")

        # prevent user changing

        #define width height
        root.geometry("430x218")

        # prevent and resizing
        root.resizable(width=False, height=False)

        # creating style
        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)

        # create grid fof the cal to sit in
        self.number_entry.grid(row=0, columnspan=4)

        # ----- first row of buttons -------

        self.button7= ttk.Button(root, text="7",
                                 command=lambda: self.button_press('7')).grid(row=1, column=0)

        self.button8= ttk.Button(root, text="8",
                                 command=lambda: self.button_press('8')).grid(row=1, column=1)

        self.button9= ttk.Button(root, text="9",
                                 command=lambda: self.button_press('9')).grid(row=1, column=2)

        self.button_div= ttk.Button(root, text="/",
                                 command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # ----- second row buttons -----

        self.button4 = ttk.Button(root, text="4",
                                 command=lambda: self.button_press('4')).grid(row=2, column=0)

        self.button5 = ttk.Button(root, text="5",
                                 command=lambda: self.button_press('5')).grid(row=2, column=1)

        self.button6 = ttk.Button(root, text="6",
                                 command=lambda: self.button_press('6')).grid(row=2, column=2)

        self.button_mult = ttk.Button(root, text="*",
                                 command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # ---- third row -----

        self.button1 = ttk.Button(root, text="1",
                                 command=lambda: self.button_press('1')).grid(row=3, column=0)

        self.button2 = ttk.Button(root, text="2",
                                 command=lambda: self.button_press('2')).grid(row=3, column=1)

        self.button3 = ttk.Button(root, text="3",
                                 command=lambda: self.button_press('3')).grid(row=3, column=2)

        self.button_add = ttk.Button(root, text="+",
                                 command=lambda: self.math_button_press('+')).grid(row=3, column=3)

        # ----  row -----

        self.button_clear = ttk.Button(root, text="AC",
                                 command=lambda: self.button_press('AC')).grid(row=4, column=0)

        self.button0 = ttk.Button(root, text="0",
                                 command=lambda: self.button_press('0')).grid(row=4, column=1)

        self.button_equal = ttk.Button(root, text="=",
                                 command=lambda: self.equal_button_press()).grid(row=4, column=2)

        self.button_sub = ttk.Button(root, text="-",
                                 command=lambda: self.math_button_press('-')).grid(row=4, column=3)



root = Tk()

calc = Calculator(root)

root.mainloop()