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

    def check_employee_status(self, day):
        """
        Description:
        Checks whether the employee is full-time, part-time, or absent.
        parameter:
        day: int which day 
        return:
        tuple: (status: str, hours: int)
        """
        check_time = random.randint(0, 1)
        if check_time == 1:
            return f"Employee is Present on day {day} and is working full time.", self.full_time_hours
        else:
            return f"Employee is Present but working part-time on day {day}.", self.part_time_hours

    def calculate_daily_wage(self, hours_worked):
        """
        Description:
        Calculates daily wage based on hours worked.
        parameter:
        hours_worked: int number of hours worked
        return:
        int: daily wage
        """
        return self.wage_per_hour * hours_worked

    def calculate_monthly_wage(self, number_of_days):
        """
        Description:
        Calculates the total monthly wage based on the number of days worked.
        parameter:
        number_of_days: int number of days worked
        return:
        tuple: (total_wage: int, total_days: int)
        """
        total_wage = 0
        total_days = 0

        for day in range(1, number_of_days + 1):
            status, hours_worked = self.check_employee_status(day)
            daily_wage = self.calculate_daily_wage(hours_worked)
            total_wage += daily_wage
            total_days += 1

        return total_wage, total_days

def main():
    print("--------Welcome to Employee Wage Computation--------")
    number_of_days = int(input("Enter the Number of Days: "))
    calculator = EmployeeWageCalculator()
    total_wage, total_days = calculator.calculate_monthly_wage(number_of_days)

    
    print(f"\nThe total monthly wage of the employee for {total_days} days is: {total_wage}")

if __name__ == "__main__":
    main()
