"""
Created on 2/7/2024
@author: Eli Jordan
"""
import pandas as pd
import tkinter as tk
import customtkinter as ctk
from ctk_listbox import *

ctk.set_appearance_mode("System")

employees_df = pd.read_csv('coffee_history.csv')

root = ctk.CTk()
root.geometry("500x500")
root.title("Whose Turn is it Anyways?")

root.resizable(False, False)

listbox = tk.Listbox(root, selectmode="multiple")
listbox.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)
i = 0
for employee in employees_df.loc[:,"Employee"]:
    listbox.insert(i, employee)
    i += 1

button = ctk.CTkButton(root, text="Stir the Pot", command=lambda:
print(employees_df[employees_df["Dollars Spent"] == min(employees_df.loc[list(listbox.curselection()),"Dollars Spent"])].loc[:,"Employee"].values[0]))

button.place(relx=0.5, rely=0.5)






if __name__ == '__main__':
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
