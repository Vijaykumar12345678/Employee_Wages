'''
@Author:Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title : python program to Calculate Wages till a condition of total working hours or days is reached for a month.

'''
import random

WAGE_PER_HOUR = 20
FULL_TIME = 8
PART_TIME = 4
MONTH_WORKING_DAYS = 20
MAXIMUM_WORKING_HOURS=100


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
        total_wage  : int Monthly wage
        daily_wage : dict daily wages
        tot_working_hours:int  total working hours
        tot_working_days: int  total working days

    """
    total_wage = 0
    daily_wages={}
   

    tot_working_hours, tot_working_days =  0, 0
    while tot_working_hours < MAXIMUM_WORKING_HOURS and tot_working_days < MONTH_WORKING_DAYS:
        status= check_employee()
        if status != "Absent":
            if status=="full-time Present":
                
                tot_working_hours+=FULL_TIME
                total_wage += WAGE_PER_HOUR * FULL_TIME
                daily_wages[f"Day_{tot_working_days+1}"]=WAGE_PER_HOUR*FULL_TIME
            else:
                tot_working_hours+=PART_TIME
                total_wage+=WAGE_PER_HOUR*PART_TIME
                daily_wages[f"Day_{tot_working_days+1}"]=WAGE_PER_HOUR*PART_TIME
            tot_working_days+=1
        else:
            tot_working_days+=1
            daily_wages[f"Day_{tot_working_days}"]=0
    


    return   total_wage,daily_wages,tot_working_hours,tot_working_days

def main():
    
    print("-------Welcome to Employee Wage Computation-------")
    
    total_wage,daily_wages,tot_working_hours,tot_working_days = calculate_wages_for_month()
    print(f"The Total working days: {tot_working_days}")
    print(f"The Total working hours: {tot_working_hours}")
    print(f"The Daily Wages:\n{daily_wages}")
    print(f"Total monthly wage: RS.{total_wage}")

if __name__ == "__main__":
    main()
