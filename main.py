import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Scientific Calculator")
        self.geometry("400x600")
        self.configure(bg="black")
        self.expression = ""
        self.create_widgets()
        # Bind keyboard events to handle numpad and other key inputs
        self.bind("<Key>", self.on_key_press)

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right",
                              bg="black", fg="white", insertbackground="white")
        self.entry.pack(side="top", fill="both", padx=10, pady=10, ipady=10)

        button_frame = tk.Frame(self, bg="black")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            # Row 1: scientific functions
            ("sin", 1, 0), ("cos", 1, 1), ("tan", 1, 2), ("log", 1, 3), ("ln", 1, 4),
            # Row 2
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("√", 2, 4),
            # Row 3
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("^", 3, 4),
            # Row 4
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("(", 4, 4),
            # Row 5
            ("0", 5, 0), (".", 5, 1), ("pi", 5, 2), ("+", 5, 3), (")", 5, 4),
            # Row 6
            ("C", 6, 0), ("DEL", 6, 1), ("exp", 6, 2), ("e", 6, 3), ("=", 6, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 16), bd=5, relief=tk.RIDGE,
                                bg="dim gray", fg="white", activebackground="gray", activeforeground="white",
                                command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(1, 7):
            button_frame.rowconfigure(i, weight=1)
        for j in range(5):
            button_frame.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, tk.END)
            self.expression = ""
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
        elif char == "=":
            try:
                result = str(self.evaluate_expression(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char in ("sin", "cos", "tan", "log", "ln", "√", "exp"):
            try:
                # Evaluate the current entry value as a float
                value = float(self.entry.get())
                if char == "sin":
                    result = math.sin(math.radians(value))
                elif char == "cos":
                    result = math.cos(math.radians(value))
                elif char == "tan":
                    result = math.tan(math.radians(value))
                elif char == "log":
                    result = math.log10(value)
                elif char == "ln":
                    result = math.log(value)
                elif char == "√":
                    result = math.sqrt(value)
                elif char == "exp":
                    result = math.exp(value)
                result = str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char in ("pi", "e"):
            self.expression += char
            self.entry.insert(tk.END, char)
        elif char == "^":
            self.expression += "**"
            self.entry.insert(tk.END, "**")
        else:
            self.expression += char
            self.entry.insert(tk.END, char)

    def evaluate_expression(self, expression):
        allowed_names = {"__builtins__": None}
        allowed_names.update(math.__dict__)
        return eval(expression, allowed_names)

    def on_key_press(self, event):
        # Mapping for numpad keys and common keys to calculator inputs
        mapping = {
            'KP_0': '0',
            'KP_1': '1',
            'KP_2': '2',
            'KP_3': '3',
            'KP_4': '4',
            'KP_5': '5',
            'KP_6': '6',
            'KP_7': '7',
            'KP_8': '8',
            'KP_9': '9',
            'KP_Decimal': '.',
            'KP_Add': '+',
            'KP_Subtract': '-',
            'KP_Multiply': '*',
            'KP_Divide': '/',
        }
        keysym = event.keysym

        if keysym in mapping:
            self.on_button_click(mapping[keysym])
        elif event.char in "0123456789.+-*/()":
            self.on_button_click(event.char)
        elif keysym == "Return":
            self.on_button_click("=")
        elif keysym == "BackSpace":
            self.on_button_click("DEL")
        elif keysym == "Delete":
            self.on_button_click("C")
        # Optionally, bind other keys for scientific functions if desired
        elif keysym.lower() in ("s", "c", "t", "l", "e"): 
            # Map first letters to their respective functions: 
            # s: sin, c: cos, t: tan, l: ln, e: exp (if desired)
            mapping_func = {
                's': "sin",
                'c': "cos",
                't': "tan",
                'l': "ln",
                'e': "exp"
            }
            self.on_button_click(mapping_func[keysym.lower()])

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()