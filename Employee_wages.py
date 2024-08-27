'''
@Author: Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title: Python program to check employee presence (full-time or part-time) and calculate wages.
'''

import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4

def check_employee():
    """
    Description:
        This function checks if the employee is present or absent, and calculates the wages for full-time or part-time employees using match-case.
    
    Parameters:
        None
    
    Returns:
        "Present" : string If the employee present
        "Absent" : string If the employee absent
    """
    
    employee = random.randint(0, 1)
    if employee==1:
        check_time=random.randint(0,1)
        if check_time==0:
            return "FullTime"
        else:
            return "PartTime"
        
    else:
        return "Absent"

def calculate_wage(hours):
    """
    Description:
        This function calculates the wage based on the number of hours worked.
    
    Parameters:
        hours : int The number of hours the employee worked.
    
    Returns:
        int: The calculated wage.
    """
    return WAGE_PER_HOUR * hours

def main():
    
    print("--------Welcome to Employee Wage Computation-------")    
    status=check_employee()
    
    match status:
         
        case "FullTime":
            print(f"The Employee is Fulltime present  and the wage is {calculate_wage(FULL_TIME)}")
  
        case"PartTime":
            print(f"The Employee is Parttime present  and the wage is {calculate_wage(PART_TIME)}") 
  
        case "Absent":
            print(f"The Employee is Absent and wage is 0")
        

if __name__ == "__main__":
    main()
