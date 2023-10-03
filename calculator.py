import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, width=20, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, padx=20, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        equal_button = tk.Button(self, text="=", padx=20, pady=20, command=self.calculate)
        clear_button = tk.Button(self, text="C", padx=20, pady=20, command=self.clear)
        delete_button = tk.Button(self, text="←", padx=20, pady=20, command=self.delete_last)

        buttons = [clear_button, delete_button, equal_button]
        for i, button in enumerate(buttons):
            button.grid(row=i+1, column=4, sticky="nsew")

    def button_click(self, char):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(char))

    def clear(self):
        self.entry.delete(0, tk.END)

    def delete_last(self):
        current = self.entry.get()
        if current:
            self.entry.delete(len(current) - 1)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop() 
