from tkinter import *
from tkinter import messagebox
import re
 
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")
 
def validate_login_fields():
    username = username_entry.get()
    password = password_entry.get()
 
    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
 
    # Validate password format
    if not re.match(r"^(?=.*[A-Z])(?=.*[a-z].*[a-z])(?=.*[^a-zA-Z0-9]).{5,10}$", password):
        messagebox.showerror("Error", "Password must contain at least 1 uppercase letter, at least 2 lowercase letters, at least 1 special character, and be between 5 and 10 characters in length.")
        return
 
    save_login_info()
    open_calculator()
 
def clear_all_fields():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
def save_login_info():
    username = username_entry.get()
    password = password_entry.get()
    with open("login_info.txt", "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
 
def open_calculator():
    calculator_window = Tk()
    calculator_window.title("Interest Calculator")
    calculator_window.geometry("400x400")
    calculator_window.configure(background='light grey')
 
    label1 = Label(calculator_window, text="Principal Amount (ZAR):", fg='black', bg='light grey')
    label2 = Label(calculator_window, text="Rate (%):", fg='black', bg='light grey')
    label3 = Label(calculator_window, text="Time (years):", fg='black', bg='light grey')
    label4 = Label(calculator_window, text="Interest Type:", fg='black', bg='light grey')
    label5 = Label(calculator_window, text="Interest Amount:", fg='black', bg='light grey')
    label6 = Label(calculator_window, text="Total Amount (Principal + Interest):", fg='black', bg='light grey')
 
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=4, column=0, padx=10, pady=10)
    label5.grid(row=5, column=0, padx=10, pady=10)
    label6.grid(row=6, column=0, padx=10, pady=10)
 
    principal_var = DoubleVar()
    principal_field = Entry(calculator_window, textvariable=principal_var)
    principal_field.grid(row=1, column=1, padx=10, pady=10)
 
    rate_field = Entry(calculator_window)
    time_field = Entry(calculator_window)
    result_field = Entry(calculator_window, state='disabled')
    total_amount_field = Entry(calculator_window, state='disabled')
 
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    result_field.grid(row=5, column=1, padx=10, pady=10)
    total_amount_field.grid(row=6, column=1, padx=10, pady=10)
 
    interest_type = StringVar()
    interest_type.set("Simple Interest")  # Default value
 
    interest_dropdown = OptionMenu(calculator_window, interest_type, "Simple Interest", "Compound Interest")
    interest_dropdown.grid(row=4, column=1, padx=10, pady=10)
 
    def calculate_interest():
        principal_text = principal_field.get()
        rate_text = rate_field.get()
        time_text = time_field.get()
 
        if not principal_text or not rate_text or not time_text:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
 
        try:
            principal = float(principal_text)
            rate = float(rate_text)
            time = float(time_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Principal, Rate, and Time.")
            return
 
        if principal <= 0 or rate <= 0 or time <= 0:
            messagebox.showerror("Error", "Please enter positive values for Principal, Rate, and Time.")
            return
 
        # Perform the calculation
        if interest_type.get() == "Simple Interest":
            simple_interest = (principal * rate * time) / 100
            total_amount = principal + simple_interest
            result_field.config(state='normal')
            result_field.delete(0, END)
            result_field.insert(0, "{:.2f}".format(simple_interest))
            result_field.config(state='disabled')
            total_amount_field.config(state='normal')
            total_amount_field.delete(0, END)
            total_amount_field.insert(0, "{:.2f}".format(total_amount))
            total_amount_field.config(state='disabled')
        elif interest_type.get() == "Compound Interest":
            compound_interest = principal * (pow((1 + rate / 100), time)) - principal
            total_amount = principal + compound_interest
            result_field.config(state='normal')
            result_field.delete(0, END)
            result_field.insert(0, "{:.2f}".format(compound_interest))
            result_field.config(state='disabled')
            total_amount_field.config(state='normal')
            total_amount_field.delete(0, END)
            total_amount_field.insert(0, "{:.2f}".format(total_amount))
            total_amount_field.config(state='disabled')
 
        # Save calculation details to file
        with open("calculation_info.txt", "a") as file:
            file.write(f"Principal Amount: {principal}\n")
            file.write(f"Rate: {rate}\n")
            file.write(f"Time: {time}\n")
            file.write(f"Interest Type: {interest_type.get()}\n")
            file.write(f"Interest Amount: {result_field.get()}\n")
            file.write(f"Total Amount: {total_amount_field.get()}\n\n")
 
    calculate_button = Button(calculator_window, text="Calculate", command=calculate_interest)
    calculate_button.grid(row=7, column=1, pady=10)
 
    calculator_window.mainloop()
 
def clear_all_and_restart():
    clear_all_fields()
    login_window.deiconify()
 
login_window = Tk()
login_window.title("Login Page")
login_window.geometry("300x300")
 
username_label = Label(login_window, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
 
username_entry = Entry(login_window)
username_entry.grid(row=0, column=1, padx=10, pady=10)
 
password_label = Label(login_window, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
 
password_entry = Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
 
show_password_var = BooleanVar()
show_password_checkbox = Checkbutton(login_window, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.grid(row=2, columnspan=2, padx=10, pady=5)
 
login_button = Button(login_window, text="Login", command=validate_login_fields)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
 
login_window.mainloop()
