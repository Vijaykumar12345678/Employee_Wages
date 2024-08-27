'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to calculate the daily wages for the employee.

'''

import random
WAGE_PER_HOUR=20
FULL_TIME=8

def check_employee():
    """
    Description:
    This funtion is to check that employee is present or absent.
    parameters:
    None
    return:
    string: present or absent """
    employee=random.randint(0,1)
    
    if employee==1:
        return "Present"
    else:
        return "Absent"
        
def calculate_wages():
    """
    Description:
    This function is used to calculate the wages of the Employee
    
    parameters:
    None
    
    return:
    int :  wages of the employee """

    
    return WAGE_PER_HOUR*FULL_TIME
        
    
def main():

    print("""-------Welcome to Employee Wage Computation-------""")
    #checking the attendance

    status=check_employee()
    #calculating the wages
    wages=calculate_wages()
    if status=="Present":
        print(f"The Employee is Present and employee wage is {wages} ")
    else:
        print("The Employee is Absent and Employee wage is 0")    

if __name__=="__main__":
    main()


