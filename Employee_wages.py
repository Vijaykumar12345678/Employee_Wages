'''
@Author: Vijay Kumar M N
@Date: 2024-08-13
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-13
@Title: Python program to Calculate Wages till a condition of total working hours or days is reached for a month.
'''

import random

class EmployeeWageCalculator:
    def __init__(self, wage_per_hour=20, full_time_hours=8, part_time_hours=4):
        self.wage_per_hour = wage_per_hour
        self.full_time_hours = full_time_hours
        self.part_time_hours = part_time_hours
        self.monthly_wage = 0
        self.total_days = 0

    def check_employee_status(self, day):
        """
        Description:
        Checks whether the employee is full-time, part-time, or absent.
        parameter:
        day: int which day 
        return:
        int : working hours
        """
        check_time = random.randint(0, 1)
        if check_time == 1:
            print(f"Employee is Present on day {day} and is working full time.")
            return self.full_time_hours
        else:
            print(f"Employee is Present but working part-time on day {day}.")
            return self.part_time_hours

    def calculate_daily_wage(self, hours_worked):
        """
        Description:
        Calculates daily wage based on hours worked.
        parameter:
        hours_worked: int its will display the full time working hour or part time working hour
        return:
        int : which multiplacation of wage per hour and hours worked"""
        return self.wage_per_hour * hours_worked

    def calculate_monthly_wage(self, number_of_days):
        """
        Description:
        Calculates the total monthly wage based on number of days worked.
        parameter:
        number_of_days: int how many days he is working.
        return :
        None"""
        print("Welcome to Employee Wage Computation")
        for day in range(1, number_of_days + 1):
            hours_worked = self.check_employee_status(day)
            daily_wage = self.calculate_daily_wage(hours_worked)
            self.monthly_wage += daily_wage
            self.total_days += 1
            print(f"The daily wage of Employee is: {daily_wage}\n")
        
        print(f"\nThe total monthly wage of the employee for {self.total_days} days is: {self.monthly_wage}")

def main():
    number_of_days = int(input("Enter the Number of Days: "))
    calculator = EmployeeWageCalculator()
    calculator.calculate_monthly_wage(number_of_days)

if __name__ == "__main__":
    main()
