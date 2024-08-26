'''

@Author:Vijay Kumar M N
@Date: 2024-08-4
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-14
@Title : python program to ability to save the total wage for each company

'''
import random

class EmpWageBuilder:
    def __init__(self):
        self.companies = {}

    def set_company_details(self, company_name, wage_per_hour, working_days):
        """
        Description:
        Sets the details for a company.
        
        Parameters:
        company_name : string Name of the company.
        wage_per_hour : int  Wage per hour for the company.
        working_days : int  Number of working days in a month for the company.
        """
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.working_days = working_days

    def calculate_wage(self):
        """
        Calculates the monthly wage and total working hours for the company.
        
        Returns:
        tuple: (company_name, total_wage, total_working_hours)
        """
        total_working_hours = 0
        total_wage = 0
        
        for day in range(self.working_days):
            status = random.choice(["full-time", "part-time", "absent"])
            
            if status == "full-time":
                daily_hours = 8
            elif status == "part-time":
                daily_hours = 4
            else:
                daily_hours = 0

            daily_wage = daily_hours * self.wage_per_hour
            total_wage += daily_wage
            total_working_hours += daily_hours

        return self.company_name, total_wage, total_working_hours

    def add_company(self):
        """
        Adds a company to the dictionary if it doesn't already exist.
        
        Returns:
        str: Message about the operation result.
        """
        if self.company_name in self.companies:
            return f"The company name {self.company_name} is already present."
        
        company_name, total_wage, total_working_hours = self.calculate_wage()
        self.companies[self.company_name] = {
            'total_wage': total_wage,
            'total_working_hours': total_working_hours
        }
        return f"{company_name} - Total Working Hours: {total_working_hours}, Total Wage: {total_wage}"

    def show_companies(self):
        """
        Shows the details of all companies.
        
        Returns:
        str: Summary of all companies.
        """
        if not self.companies:
            return "No companies have been added yet."
        
        summary = "Summary of all companies:\n"
        for company, details in self.companies.items():
            summary += f"{company} - Total Working Hours: {details['total_working_hours']}, Total Wage: {details['total_wage']}\n"
        return summary

def main():
    builder = EmpWageBuilder()

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
            
            builder.set_company_details(company_name, wage_per_hour, working_days)
            result = builder.add_company()
            print(result)

        elif choice == "2":
            result = builder.show_companies()
            print(result)

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
