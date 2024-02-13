"""
Created on 2/7/2024
@author: Eli Jordan
"""
import pandas as pd
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
_DEBUG = False


class App(ctk.CTk):
    # class to contain CTk app
    def __init__(self, file_path:str = "coffee_history.csv"):
        super().__init__()
        # open csv as dataframe
        self.employees_df = pd.read_csv(file_path)
        # window setup
        self.geometry("400x300")
        self.title("Whose Turn is it Anyways?")
        self.resizable(False, False)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.instantiate_listbox()
        # add names to listbox
        self.employee_chosen_output = ctk.CTkTextbox(self)
        self.employee_chosen_output.grid(column=0, row=1, sticky="")

        # create button
        self.button = ctk.CTkButton(self, text="Stir the Pot", command=self.button_callback)
        self.button.grid(column=1, row=1, sticky="ew")

        # reference for employee selected
        self.selected_employee = ""

    def button_callback(self):
        # clear textbox
        self.employee_chosen_output.delete("0.0", ctk.END)
        # find employee with least spent
        self.selected_employee = self.employees_df[self.employees_df["Dollars Spent"] == min(self.employees_df.loc[list(self.listbox.curselection()), "Dollars Spent"])].loc[:, "Employee"].values[0]
        # update text box
        self.employee_chosen_output.insert("0.0", self.selected_employee)
        # sum employees' coffee order
        self.sum_coffee_order(list(self.listbox.curselection()))

    def instantiate_listbox(self):
        self.listbox = tk.Listbox(self, selectmode="multiple")
        self.listbox.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)
        self.listbox.grid(column=0, row=0, sticky="nsew")

        i = 0
        for employee in self.employees_df.loc[:, "Employee"]:
            self.listbox.insert(i, employee)
            i += 1

    def sum_coffee_order(self, employees: list):
        coffee_prices = {
            "Black": 3.0,
            "Mocha": 5.0,
            "Frappe": 5.50,
            "Cappuccino": 4.50,
            "Americano": 4.0,
            "Tea": 3.50,
            "Soda": 4.25
        }

        # coffee_prices = pd.DataFrame.from_dict(coffee_prices, orient="index",columns=["coffee_price"])
        # define the coffees we need
        coffee_total = 0
        coffee_order = list(self.employees_df.loc[employees, "Favorite Drink"])
        if _DEBUG:
            print(coffee_order)
        for coffee in coffee_order:
            coffee_total += coffee_prices[coffee]
        if _DEBUG:
            print(coffee_total)
        # update selected employees spent total
        self.employees_df.loc[self.employees_df[self.employees_df["Employee"] == self.selected_employee].index.values[0], "Dollars Spent"] += coffee_total
        if _DEBUG:
            print(self.employees_df.loc[self.employees_df[self.employees_df["Employee"] == self.selected_employee].index.values[0], "Dollars Spent"])
        # write updated dataframe to csv file
        self.employees_df.to_csv("coffee_history.csv", index=False)


if __name__ == '__main__':
    app = App()
    app.mainloop()