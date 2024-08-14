'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to calculate the daily wages for the employee.

'''
import random
def check_employee(employee):
    """
    Description:
    This funtion is to check that employee is present or absent.
    parameters:
    employee : int which is to check if it is 1 then present  or else absent.
    return:None """
    
    print("""Welcome to Employee Wage Computation""")
    if employee==1:
        
        wage_per_hour=20
        full_day=8
        daily_wage=wage_per_hour*full_day
        print(f"The Employee is Present and employee wage is {daily_wage} ")
    else:
        print("The Employee is Absent and Employee wage is 0")
def main():
    number=random.randint(0,1)
    check_employee(number)

if __name__=="__main__":
    main()



