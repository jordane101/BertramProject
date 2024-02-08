"""
Created on 2/7/2024
@author: Eli Jordan
"""
import pandas as pd

employees = pd.read_csv('coffee_history.csv')

print(employees)

if __name__ == '__main__':
    ready = False
    while not ready:
        # gather information loop
        read = input("Who is going to the coffee shop? (ALL for everyone):")
        match read:
            case "ALL":
                ready = True
                print("All the coffee")
            case _ :
                print("Invalid input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
