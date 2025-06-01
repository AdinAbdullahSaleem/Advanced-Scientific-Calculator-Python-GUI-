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

    def create_widgets(self):
        self.entry = tk.Entry(self, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right", bg="gray", fg="white")
        self.entry.pack(side="top", fill="both", padx=10, pady=10, ipady=10)

        button_frame = tk.Frame(self, bg="black")
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sin", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("cos", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("tan", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("(", 4, 2), (")", 4, 3), ("+", 4, 4),
            ("C", 5, 0), ("DEL", 5, 1), ("^", 5, 2), ("√", 5, 3), ("=", 5, 4)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 16), bd=5, relief=tk.RIDGE,
                               command=lambda t=text: self.on_button_click(t), bg="gray", fg="black")
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(6):
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
        elif char in ("sin", "cos", "tan", "√"):
            try:
                value = float(self.entry.get())
                if char == "sin":
                    result = str(math.sin(math.radians(value)))
                elif char == "cos":
                    result = str(math.cos(math.radians(value)))
                elif char == "tan":
                    result = str(math.tan(math.radians(value)))
                elif char == "√":
                    result = str(math.sqrt(value))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
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

if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()