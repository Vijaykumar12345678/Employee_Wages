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
    def calculate_wage(cls, wage_per_hour, working_days):
        """
        Description:
        This function calculates the total monthly wage and total working hours for a company.
        
        Parameters:
        wage_per_hour : int  Wage per hour.
        working_days : int Number of working days in a month.
        
        Returns:
        tuple: Total wage and total working hours for the month.
        """
        total_working_hours = 0
        total_wage = 0
        
        for day in range(working_days):
            status = random.choice(["full-time", "part-time", "absent"])
            
            if status == "full-time":
                daily_hours = 8
            elif status == "part-time":
                daily_hours = 4
            else:
                daily_hours = 0

            # Calculate the wage for the day
            daily_wage = daily_hours * wage_per_hour
            total_wage += daily_wage
            total_working_hours += daily_hours

        return total_wage, total_working_hours

def add_company(companies, company_name, wage_per_hour, working_days):
    """
    Description:
    Adds a new company to the list and calculates its wage details.
    
    Parameters:
    companies : dict Dictionary of companies and their wage details.
    company_name : string Name of the company to add.
    wage_per_hour : int Wage per hour for the company.
    working_days : int Number of working days in a month for the company.
    
    Returns:
    None
    """
    if company_name in companies:
        return f"The company name {company_name} is already present."
    
    total_wage, total_working_hours = EmpWageBuilder.calculate_wage(wage_per_hour, working_days)
    
    companies[company_name] = {
        'total_wage': total_wage,
        'total_working_hours': total_working_hours
    }
    return f"{company_name} - Total Working Hours: {total_working_hours}, Total Wage: {total_wage}"

def display_companies(companies):
    """
    Description:
    Displays the summary of all companies and their wage details.
    
    Parameters:
    companies : dict Dictionary of companies and their wage details.
    
    Returns:
    None
    """
    if not companies:
        return "No companies have been added yet."
    
    summary = "Summary of all companies:\n"
    for company, details in companies.items():
        summary += f"{company} - Total Working Hours: {details['total_working_hours']}, Total Wage: {details['total_wage']}\n"
    return summary

def main():
    companies = {}

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Show company wages")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
            working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
            result = add_company(companies, company_name, wage_per_hour, working_days)
            print(result)

        elif choice == "2":
            result = display_companies(companies)
            print(result)

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
