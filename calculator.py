import tkinter as tk
LARGE_FONT_STYLE = ('Arial', 40, 'bold')
DIGITS_FONT_STYLE = ('Arial', 24, 'bold')
SMALL_FONT_STYLE = ('Arial', 16, 'bold')
NORMAL_FONT_STYLE = ('Arial', 20, 'bold')
pink = "#eba09b"
yellow = "#f2eb5a"
blue = "#81e3d9"
green = "#a0eb6e"
purple = "#d58df0"
black = "#000000"
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("калькулятор")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = ""
        self.current_expression = ""
        self.digits = {7: (1,1), 8: (1, 2), 9:(1, 3),
                       4:(2,1), 5:(2,2), 6:(2,3),
                       1:(3,1), 2:(3,2), 3:(3,3), 0:(4,1), ".": (4,2)}
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_sqrt_button()
        self.create_square_button()
        self.create_clear_button()
        self.create_equal_button()
        self.buttons_frame.rowconfigure(0, weight= 1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight= 1)
            self.buttons_frame.columnconfigure(x, weight= 1)
        self.total_label, self.label = self.create_display_label()
    def create_display_frame(self):
        frame = tk.Frame(self.window, height = 221)
        frame.pack(expand = True, fill = "both")
        return frame
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand = True, fill = "both")
        return frame
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text = str(digit), bg = blue, fg = black, font = DIGITS_FONT_STYLE, command = lambda x = digit:
                               self.add_expression(x))
            button.grid(row = grid_value[0], column = grid_value[1], sticky = tk.NSEW)
    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = operator, bg = blue, fg = black, font = DIGITS_FONT_STYLE, command = lambda x = operator:
                               self.add_operator(x))
            button.grid(row = i, column = 4, sticky = tk.NSEW)
            i += 1
    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression} **0,5"))
        self.update_label()
    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text = "\u221ax", bg = blue, fg = black, font = DIGITS_FONT_STYLE, command= self.sqrt)
        button.grid(row = 0, column = 3, sticky = tk.NSEW)
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression} **2"))
        self.update_label()
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text = "x\u00b2", bg = blue, fg = black, font = DIGITS_FONT_STYLE, command = self.square)
        button.grid(row = 0, column = 2, sticky = tk.NSEW)
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text = "C", bg = blue, fg = black, font = DIGITS_FONT_STYLE, command = self.clear)
        button.grid(row = 0, column = 1, sticky = tk.NSEW)
    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text = "=", bg = blue, fg = black, font = DIGITS_FONT_STYLE, command = self.equal)
        button.grid(row = 4, column = 3, columnspan = 2, sticky = tk.NSEW)

    def equal(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
            self.update_total_label()
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text = self.total_expression, font = SMALL_FONT_STYLE, bg = purple)
        total_label.pack(expand = True, fill = "both")
        label = tk.Label(self.display_frame, self.current_expression, font = LARGE_FONT_STYLE, bg = purple)
        label.pack(expand= True, fill = "both")
        return total_label, label
    def add_expression(self, value):
        self.current_expression += str(value)
        self.update_label()
    def add_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_label()
        self.update_total_label()
    def update_total_label(self):
        expression = self.total_expression
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator, f"{symbol}")
        self.total_label.config(text = expression)
    def update_label(self):
        self.label.config(text=self.current_expression[:11])
        

        
    def run(self):
        self.window.mainloop()
calc = Calculator()
calc.run()


