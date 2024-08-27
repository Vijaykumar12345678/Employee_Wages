'''
@Author: Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title: Python program to check employee presence (full-time or part-time) and then calculate the monthly wages.
'''

import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
MONTH_WORKING_DAYS = 20

def check_employee():
    """
    Description:
    This function checks if the employee is present or absent and returns their status along with the daily and monthly wages.
    
    parameters:
    None 

    Returns:
    tuple: A tuple containing the employee status, daily wage, and monthly wage.
    """
   
    employee = random.randint(0, 1)
    if employee == 1:
        check_time = random.randint(0, 1)
        if check_time == 0:
            daily_wage, monthly_wage = calculate_wages(PART_TIME)
                
            return "part-time Present", daily_wage, monthly_wage
                
        else:
            daily_wage, monthly_wage = calculate_wages(FULL_TIME)
            return "full-time Present", daily_wage, monthly_wage
            
    else:
        return "Absent", 0, 0
 
def calculate_wages(hours):
    """
    Description:
    This function calculates the daily wage and monthly wage based on the number of hours worked.
    
    Parameters:
    hours : int The number of hours the employee worked.
    
    Returns:
    tuple: A tuple containing the daily wage and the monthly wage.
    """
    daily_wage = WAGE_PER_HOUR * hours
    monthly_wage = daily_wage * MONTH_WORKING_DAYS
    return daily_wage, monthly_wage

def main():
    print("-------Welcome to Employee Wage Computation-------")
    
    status, daily_wage, monthly_wage = check_employee()
    print(f"The Employee is {status} and employee daily wage is {daily_wage}")
    print(f"The Employee is {status} and monthly wage is {monthly_wage}")

if __name__ == "__main__":
    main()
