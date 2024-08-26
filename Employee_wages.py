'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to check employee present full time or part and then calculate the wages.

'''
import random

WAGE_PER_HOUR=20
FULL_TIME=8
PART_TIME=4
def check_employee():
    """
    Description:
    This funtion is to check that employee is present or absent and calculate the wages for the full time employee and part time employee.
    
    parameters:
    None
    
    return:
    None """
    employee=random.randint(0,1)

    
    if employee==1:
        check_time=random.randint(0,2)
        if check_time==0:
            return "Present"
        else:
            return "Parttime"
        
    else:
        return "Absent"

def calculate_wages(check_time):
    """
    Description:
    This function is used to calculate the wages of the Employee
    
    parameters:
    wage_per_time: int  which is the wage per hour of the employee
    check_time: int which is the time for which the employee is present
    
    return:
    int:calculated the wages   """
    return  WAGE_PER_HOUR *check_time       

def main():
    print("""-------Welcome to Employee Wage Computation-------""")

    #check Employee is presentot not
    employee=check_employee()
    
    #employee is full time present

    if employee=="Present":
        daily_wage=calculate_wages( FULL_TIME)
        print(f"The Employee is Present fulltime and employee wage is {daily_wage}")
    #employee is part time present
    
    elif employee=="Parttime":
        daily_wage=calculate_wages( PART_TIME)
        print(f"The Employee is Present parttime and employee wage is {daily_wage}")
    
    else:
        print(f"The Employee is Absent and employee wage is {0}")


if __name__=="__main__":
    main()



