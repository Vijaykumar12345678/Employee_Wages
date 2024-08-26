'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to Calculate Wages till a condition of total working hours or days is reached for a month.

'''
import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
MONTH_WORKING_DAYS = 20

def calculate_wages(hours):
    """
    Description:
    This function calculates the daily wage and monthly wage based on the number of hours worked.
    
    Parameters:
    hours (int): The number of hours the employee worked.
    
    Returns:
    tuple: A tuple containing the daily wage and the monthly wage.
    """
    daily_wage = WAGE_PER_HOUR * hours
    monthly_wage = daily_wage * MONTH_WORKING_DAYS
    return daily_wage, monthly_wage

def check_employee(employee):
    """
    Description:
    This function checks if the employee is present or absent and calculates the wages for full-time or part-time employees.
    
    Parameters:
    employee (int): An integer that is 1 if the employee is present or 0 if absent.
    
    Returns:
    None
    """
    print("Welcome to Employee Wage Computation")
    
    if employee == 1:
        check_time = random.randint(0, 1)
        if check_time == 0:
            daily_wage, monthly_wage = calculate_wages(PART_TIME)
            print(f"The Employee is part-time Present and employee daily wage is {daily_wage}")
            print(f"The Employee is part-time Present and monthly wage is {monthly_wage}")
        else:
            daily_wage, monthly_wage = calculate_wages(FULL_TIME)
            print(f"The Employee is full-time Present and employee daily wage is {daily_wage}")
            print(f"The Employee is full-time Present and monthly wage is {monthly_wage}")
    else:
        print("The Employee is Absent and Employee daily and monthly wage is 0")

def main():
    employee = random.randint(0, 1)
    check_employee(employee)

if __name__ == "__main__":
    main()




