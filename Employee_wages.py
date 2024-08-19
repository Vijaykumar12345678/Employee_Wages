'''

@Author:Vijay Kumar M N
@Date: 2024-08-19
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-19
@Title : python program to Ability to manage Employee Wage of multiple companies

'''
import random

class EmpWageBuilder:
    @classmethod
    def calculate_wage(cls, wage_per_hour, working_days):
        """
        Description:
        This function calculates the monthly wage for an employee.
        
        Parameters:
        wage_per_hour: int - the wage for each hour worked
        working_days: int - the number of working days in a month
        
        Returns:
        total_wage: int - the total wage for the month
        total_working_hours: int - the total hours worked in the month
        """
        total_working_hours = 0
        total_wage = 0
        
        for day in range(working_days):
            status = random.choice(["full-time", "part-time"])
            
            if status == "full-time":
                daily_hours = 8
            else:  # part-time
                daily_hours = 4

            daily_wage = daily_hours * wage_per_hour
            total_wage += daily_wage
            total_working_hours += daily_hours

        return total_wage, total_working_hours

def add_company_and_calculate_wages():
    companies = {}

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Add an employee to a company")
        print("3. Show company wages")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            if company_name in companies:
                print(f"The company name {company_name} is already present.")
            else:
                wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
                working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
                companies[company_name] = {
                    'wage_per_hour': wage_per_hour,
                    'working_days': working_days,
                    'employees': []
                }
                print(f"Company {company_name} added successfully.")

        elif choice == "2":
            company_name = input("Enter the company name to add an employee: ")
            if company_name not in companies:
                print(f"The company name {company_name} does not exist.")
            else:
                emp_name = input("Enter the employee's name: ")
                company_info = companies[company_name]
                total_wage, total_working_hours = EmpWageBuilder.calculate_wage(
                    company_info['wage_per_hour'], 
                    company_info['working_days']
                )
                
                employee_details = {
                    'name': emp_name,
                    'total_wage': total_wage,
                    'total_working_hours': total_working_hours
                }
                company_info['employees'].append(employee_details)
                print(f"\nEmployee {emp_name} added to {company_name} with Total Working Hours: {total_working_hours}, Total Wage: {total_wage}\n")

        elif choice == "3":
            if not companies:
                print("\nNo companies have been added yet.")
            else:
                print("\nSummary of all companies:")
                for company, company_info in companies.items():
                    print(f"\nCompany: {company}")
                    print(f"Wage per Hour: {company_info['wage_per_hour']}")
                    print(f"Working Days per Month: {company_info['working_days']}")
                    if not company_info['employees']:
                        print("No employees in this company.")
                    else:
                        for emp in company_info['employees']:
                            print(f"Employee: {emp['name']}, Total Working Hours: {emp['total_working_hours']}, Total Wage: {emp['total_wage']}")
                    

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    add_company_and_calculate_wages()

if __name__ == "__main__":
    main()

