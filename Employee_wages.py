'''

@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to Calculate Wages till a condition of total working hours or days is reached for a month.

'''
import random
def check_employee(number_of_days):
    """
    Description:
    This function will display the each day id the employee is part time or full time and then calculate the monthly wages .
    parameters:
    employee : int which is to check if it is 1 then present  or else absent.
    return:None """
    
    wage_per_hour=20
    full_time=8
    part_time=4
    monthly_wage=0
    daily_wage=0
    counter=0
    print("""Welcome to Employee Wage Computation""")
    
    for i in range(1,number_of_days+1):

            check_time=random.randint(0,1)
            if check_time==1:
                  print(f"Employee is Present on day and is working full time: {i}")
                  daily_wage = wage_per_hour * full_time
                  print(f"The daily wage of Employee is: {daily_wage}")
                  print(" \n ")
                  counter += 1
            elif check_time==0:
                print(f"Employee is Present but working part time on day: {i}")
                daily_wage = wage_per_hour * part_time
                print(f"The daily wage of Employee is: {daily_wage}")
                print(" \n ")
            else:
                 print(f"Employee is Absent on day: {i}")
                 daily_wage = 0
                 print(f"The daily wage of Employee is: {daily_wage}")
                 print(" \n ")
            monthly_wage+=daily_wage
    print("\n")
    
            #if total_hours >= 100 and counter >= 20:
    print(f"The monthly wage of employee is: {monthly_wage}")
            #else:
            #print(f"The monthly wage of employee is: {monthly_wage}")

def main():
    number_of_days=int(input("Enter the Number of Days: "))

    check_employee(number_of_days)

if __name__=="__main__":
    main()



