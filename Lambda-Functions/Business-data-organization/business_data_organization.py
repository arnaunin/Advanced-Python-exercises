from itertools import groupby
import json

# Read the list of employees in the json file
with open("employees.json", 'r') as employees_json:
    # Saave that list in a variable
    employees = json.load(employees_json)

# Function to sort by performance (from highest to lowest) and age (from lowest to highest) the employees
def sort_employees(employees):
    sorted_employees = sorted(employees, key=lambda emp: (emp['performance'], -emp['age']), reverse=True)
    return sorted_employees

# Function to group the employees by country
def group_by_country(sorted_employees):
    # For groupby to work first we need to sort the employees by country
    sorted_by_employees = sorted(sorted_employees, key=lambda emp: emp['country'])

    grouped_employees = {country: list(employees_group) for country, employees_group in groupby(sorted_by_employees, key=lambda emp: emp['country'])} # This is a dictionary comprehension, it is broken down below
    return grouped_employees

    """
    Dictionary comprehension broken down:

    grouped_employees = {}

    grouped_by_employees = groupby(sorted_employees, key=lambda emp: emp['country'])
    for country, employees_group in grouped_by_employees:
        grouped_employees[country] = list(employees_group)
    """

# Function to show all the employees
def show_grouped_employees(grouped_employees):
    for country, employees in grouped_employees.items():
        print("\nCountry: ", country)
        for employee in employees:
            print(employee)


sorted_employees = sort_employees(employees)
grouped_employees = group_by_country(sorted_employees)
show_grouped_employees(grouped_employees)



