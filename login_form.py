import tkinter as tk
import sqlite3
from expense import ExpenseTracker
from tkinter.messagebox import showinfo
from Registration import register
import pywhatkit
from datetime import timedelta
import datetime
from forgetPassword import ForgetPasswordWindow

conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Login Form")

        self.label_title = tk.Label(self, text="Login Form", width=20, font=("bold", 20))
        self.label_title.place(x=90, y=53)

        self.label_username = tk.Label(self, text="Username", width=17, font=("bold", 10))
        self.label_username.place(x=80, y=130)

        self.entry_username = tk.Entry(self)
        self.entry_username.place(x=240, y=130)

        self.label_password = tk.Label(self, text="Password", width=17, font=("bold", 10))
        self.label_password.place(x=68, y=170)

        self.entry_password = tk.Entry(self,show='*')
        self.entry_password.place(x=240, y=170)

        self.button_forgot_password = tk.Button(self, text='Forgot Password?', width=20, bg='black', fg='white',command=self.forget)
        self.button_forgot_password.place(x=155, y=250)

        self.button_submit = tk.Button(self, text='Submit', width=20, bg='black', fg='white',command=self.submit)
        self.button_submit.place(x=155, y=300)

        self.button_back = tk.Button(self, text='Back', width=15, bg='black', fg='white',command=self.back)
        self.button_back.place(x=50, y=450)

    def submit(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        cursor.execute("SELECT password FROM registration WHERE user = ?", (username,))
        result = cursor.fetchone()
        if result and result[0] == password:
            showinfo(title="Login",message="Logged in Successfully")
            tracker = ExpenseTracker()
            self.destroy()
        else:
            showinfo(title="Login",message="Login Failed !! Please check Username and Password")

    def back(self):
        register()
        self.destroy()


    def forget(self):
        ForgetPasswordWindow()
        self.destroy()

if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()
