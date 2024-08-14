'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to check employee is present or not.

'''
import random
def check_employee(employee):
    """
    Description:
    This funtion is to check that employee is present or absent.
    parameters:
    employee : int which is to check if it is 1 then present  or else absent.
    return:None """
    if employee==1:
        print("The Employee is Present.")
    else:
        print("The Employee is Absent")
def main():
    number=random.randint(0,1)
    check_employee(number)

if __name__=="__main__":
    main()



