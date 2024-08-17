'''

@Author:Vijay Kumar M N
@Date: 2024-08-4
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-14
@Title : python program to compute Compute Employee Wage for multiple companies

'''
import random

class EmpWageBuilder:
    @classmethod
    def calculate_wage(cls, company_name, wage_per_hour, working_days):
        """
        Description:
        This function will calculate the monthly wage for the company.
        parameter:
        company_name: string the company which we are going to calculate.
        wage_per_hour: int how much amount of wage is for per hour
        working_days: int how many working days in a month
        Return:
        company name
        working_hours and total wages in a month. """
        total_working_hours = 0
        total_wage = 0
        
        for day in range(working_days):
            status = random.choice(["full-time", "part-time"])
            
            if status == "full-time":
                daily_hours = 8
            else:  # part-time
                daily_hours = 4

            # Calculate the wage for the day
            daily_wage = daily_hours * wage_per_hour
            total_wage += daily_wage
            total_working_hours += daily_hours
            
            print(f"Day {day + 1}: {status.capitalize()} - Hours Worked: {daily_hours}, Daily Wage: {daily_wage}")

        return company_name, total_wage, total_working_hours

def add_company_and_calculate_wages():
    companies = {}

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Show company wages")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            if company_name in companies:
                print(f"The company name {company_name} is already present.")
            else:
                wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
                working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
                company_name, total_wage, total_working_hours = EmpWageBuilder.calculate_wage(
                    company_name, wage_per_hour, working_days
                )
                
                companies[company_name] = {
                    'total_wage': total_wage,
                    'total_working_hours': total_working_hours
                }
                print(f"\n{company_name} - Total Working Hours: {total_working_hours}, Total Wage: {total_wage}\n")

        elif choice == "2":
            if not companies:
                print("\ no companies have been added yet.")
            else:
                print("\nSummary of all companies:")
                for company, details in companies.items():
                    print(f"{company} - Total Working Hours: {details['total_working_hours']}, Total Wage: {details['total_wage']}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

    return companies

def main():
    
    add_company_and_calculate_wages()

if __name__ == "__main__":
    main()
