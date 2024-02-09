"""
Created on 2/7/2024
@author: Eli Jordan
"""
import pandas as pd
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")

employees_df = pd.read_csv('coffee_history.csv')

root = ctk.CTk()
root.grid_rowconfigure(2,weight=1)
root.grid_columnconfigure(2,weight=1)

root.geometry("500x500")
root.title("Whose Turn is it Anyways?")

root.resizable(False, False)

listbox = tk.Listbox(root, selectmode="multiple")
listbox.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)
listbox.grid(column=0, row=0, sticky="nsew")

i = 0
for employee in employees_df.loc[:, "Employee"]:
    listbox.insert(i, employee)
    i += 1

employee_chosen_output = ctk.CTkTextbox(root)
employee_chosen_output.grid(column=0, row=1, sticky="")

# what are these references idk what's going on
# def choose_employee():
#     try:
#         print(min(employees_df.loc[list(listbox.curselection()), "Dollars Spent"]))
#     except ValueError:
#         print("Value Error")
#         employee_chosen_output.delete("0.0", ctk.END)
#     else:
#         print("else")
#         employee_chosen_output.delete("0.0", ctk.END)
#         employee_chosen_output.insert("0.0", employees_df[employees_df["Dollars Spent"] == min(employees_df.loc[list(listbox.curselection()), "Dollars Spent"])].loc[:,"Employee"].values[0])

def sum_coffee_order(employees:list):
    coffee_prices = {
        "Black": 3.0,
        "Mocha": 5.0,
        "Frappe": 5.50,
        "Cappuccino": 4.50,
        "Americano": 4.0,
        "Tea": 3.50,
        "Soda": 4.25
    }

    coffee_prices = pd.DataFrame.from_dict(coffee_prices, orient="index",columns=["coffee_price"])
    #define the coffees we need
    coffee_total=0
    coffee_order = employees_df.loc[employees, "Favorite Drink"]
    for price in coffee_prices.loc[coffee_order]:
        coffee_total += int(price)

    employees_df.loc[employee_chosen_output.get("0.0"), "Dollars Spent"] += coffee_total

    print(coffee_total)

# button lambda function necessary because the listbox.curselection() returns null when empty
# I am so sorry for this lambda function
#I'm going to clean this up
# maybe

employees_selected = []
button = ctk.CTkButton(root, text="Stir the Pot", command=
lambda: (
    employee_chosen_output.delete("0.0",ctk.END),
    employee_chosen_output.insert("0.0", employees_df[employees_df["Dollars Spent"] == min(employees_df.loc[list(listbox.curselection()), "Dollars Spent"])].loc[:, "Employee"].values[0]),
    sum_coffee_order(list(listbox.curselection()))
))


button.grid(column=1, row=1, sticky="ew")



if __name__ == '__main__':
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
