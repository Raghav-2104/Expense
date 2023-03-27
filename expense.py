import tkinter as tk

class ExpenseTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Expense Tracker")

        self.label_title = tk.Label(self, text="Expense Tracker", width=20, font=("bold", 20))
        self.label_title.place(x=90, y=53)

        self.label_amount = tk.Label(self, text="Amount", width=17, font=("bold", 10))
        self.label_amount.place(x=80, y=130)

        self.entry_amount = tk.Entry(self)
        self.entry_amount.place(x=240, y=130)

        self.label_category = tk.Label(self, text="Category", width=17, font=("bold", 10))
        self.label_category.place(x=68, y=170)

        self.options = ["Food", "Entertainment", "Transportation", "Utilities", "Other"]
        self.selected_category = tk.StringVar(self)
        self.selected_category.set(self.options[0])
        self.dropdown_category = tk.OptionMenu(self, self.selected_category, *self.options)
        self.dropdown_category.config(width=15)
        self.dropdown_category.place(x=240, y=170)

        self.label_notes = tk.Label(self, text="Notes", width=17, font=("bold", 10))
        self.label_notes.place(x=68, y=210)

        self.text_notes = tk.Text(self, height=4, width=30)
        self.text_notes.place(x=240, y=210)

        self.button_add = tk.Button(self, text='Add Expense', width=20, bg='black', fg='white')
        self.button_add.place(x=155, y=300)

        self.button_clear = tk.Button(self, text='Clear', width=15, bg='black', fg='white')
        self.button_clear.place(x=50, y=450)

        self.button_view = tk.Button(self, text='View Expenses', width=15, bg='black', fg='white')
        self.button_view.place(x=320, y=450)


if __name__ == "__main__":
    
    app = ExpenseTracker()
    app.mainloop()
