'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to check employee present full time or part and then calculate the wages.

'''
import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME= 4


def check_employee():
    """
    Description:
    This function checks if the employee is present or absent and calculates the wages for full-time or part-time employees.
    
    Parameters:
    None
    
    Returns:
    None
    """
    
    employee = random.randint(0, 1)
    match employee:
        case 1:
            check_time = random.randint(0, 1)
            match check_time:
                case 0:
                    daily_wage = calculate_wage(PART_TIME)
                    print(f"The Employee is part-time Present and employee wage is {daily_wage}")
                case 1:
                    daily_wage = calculate_wage(FULL_TIME)
                    print(f"The Employee is full-time Present and employee wage is {daily_wage}")
        case 0:
            print("The Employee is Absent and Employee wage is 0")
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
    check_employee()

if __name__ == "__main__":
    main()
