'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to check employee is present or not.

'''
import random
def check_employee():
    """
    Description:
    This funtion is to check that employee is present or absent.
    parameters:
    None
    return:
    string: The employee is present or absent """
    employee=random.randint(0,1)
    
    if employee==1:
        return "Present"
    else:
        return "Absent"

def main():

    print("------- Welcome to Employee Wage Computation Program--------")
    #employee attendance
    status=check_employee()
    print(f"The Employee is {status}.")

if __name__=="__main__":
    main()



