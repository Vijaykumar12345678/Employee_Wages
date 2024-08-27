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
        This function checks if the employee is present and returns their status and hours worked.

    Parameters:
        None

    Returns:
        "Present" : string If the employee is present
        "Absent" : string If the employee is absent
    """
    employee = random.randint(0, 1)
    if employee == 1:
        check_time = random.randint(0, 1)
        if check_time == 0:
            return "full-time Present"
        else:
            return "part-time Present"
    else:
        return "Absent"

def calculate_wages_for_month():
    """
    Description:
        This function calculates the total monthly wage by checking each day whether the employee is present and whether they worked full-time or part-time.

    Parameters:
        None

    Returns:
        int : Monthly wage
    """
    total_wage = 0
    total_wages={}
   

    for day in range(MONTH_WORKING_DAYS):
        status= check_employee()
        if status != "Absent":
            if status=="full-time Present":
                
                
                total_wage += WAGE_PER_HOUR * FULL_TIME
                total_wages[day+1]=WAGE_PER_HOUR*FULL_TIME
            else:
                
                total_wage+=WAGE_PER_HOUR*PART_TIME
                total_wages[day+1]=WAGE_PER_HOUR*PART_TIME
    print(total_wages)


    return   total_wage

def main():
    
    print("-------Welcome to Employee Wage Computation-------")
    
    total_wage = calculate_wages_for_month()
    print(f"Total monthly wage: {total_wage}")

if __name__ == "__main__":
    main()
