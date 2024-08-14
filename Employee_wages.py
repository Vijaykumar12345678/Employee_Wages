'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to check employee present full time or part and then calculate the wages.

'''
import random
def check_employee(employee):
    """
    Description:
    This funtion is to check that employee is present or absent and calculate the wages for the full time employee and part time employee.
    parameters:
    employee : int which is to check if it is 1 then present  or else absent.
    return:None """
    
    wage_per_hour=20
    full_time=8
    part_time=4
    print("""Welcome to Employee Wage Computation""")
    match employee:
        case 1:
            check_time=random.randint(0,1)
            match check_time:
                case 0:
                    daily_wage=wage_per_hour*part_time
                    print(f"The Employee is part time Present and employee wage is {daily_wage} ")
                case _:
                    print(f"The Employee is full time Present and employee wage is {wage_per_hour*full_time}")
        case _:
            print("The Employee is Absent and Employee wage is 0")
def main():
    employee=random.randint(0,1)
    check_employee(employee)

if __name__=="__main__":
    main()



