'''

@Author:Vijay Kumar M N
@Date: 2024-08-4
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-14
@Title : python program to ability to save the total wage for each company

'''
import random

class EmpWageBuilder:
    def __init__(self, company_name, wage_per_hour, working_days, max_working_hours):
       
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.working_days = working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0
        self.total_working_hours = 0
        self.daily_wages = {}

    def get_attendance(self):
        """
        Description:
            Determines the attendance status for a day.
        
        Parameters:
            None
        
        Returns:
            tuple: (daily_hours, status)
        """
        
        
        status = random.randint(0, 1)
        if status == 1:
            check_time = random.randint(0, 1)
            if check_time == 0:
                daily_hours=8
            else:
                daily_hours=4
        else:
            daily_hours=0
            
        return daily_hours, status

    def calculate_wage(self):
        """
        Description:
            Calculates the monthly wage and total working hours for the company.
            Also stores the daily wages in a dictionary format.
        Parameters:
            None
        
        Returns:
            None
        """
        day = 1
        while day <= self.working_days and self.total_working_hours < self.max_working_hours:
            daily_hours, status = self.get_attendance()
            
            # Ensure that adding daily_hours doesn't exceed max_working_hours
            if self.total_working_hours + daily_hours > self.max_working_hours:
                daily_hours = self.max_working_hours - self.total_working_hours
            
            daily_wage = daily_hours * self.wage_per_hour
            self.daily_wages[f"Day {day}"] = daily_wage
            self.total_wage += daily_wage
            self.total_working_hours += daily_hours
            day += 1

    def get_company_summary(self):
        """
        Description:
            Returns a summary of the company with total wage, working hours, and daily wages.
        
        Parameters:
            None
        
        Returns:
            str: Summary of the company's wage, working hours, and daily wages.
        """
        summary = f"{self.company_name} - Total Working Hours: {self.total_working_hours}, Total Wage: {self.total_wage}\n"
        summary += "Daily Wages:\n"
        summary += "{\n"
        for day, wage in self.daily_wages.items():
            summary += f"  {day}: {wage}\n"
        summary += "}\n"
        return summary

class EmpWageManager:
    def __init__(self):
        self.companies = {}

    def add_company(self, company_name, wage_per_hour, working_days, max_working_hours):
        """
        Description:

            Adds a new company to the manager.
        
        Parameters:
            company_name : str  Name of the company.
            wage_per_hour : int  Wage per hour for the company.
            working_days : int  Number of working days in a month for the company.
            max_working_hours : int  Maximum working hours allowed for the company.
        
        Returns:
            str: Message about the operation result.
        """
        if company_name in self.companies:
            return f"The company name {company_name} is already present."

        company = EmpWageBuilder(company_name, wage_per_hour, working_days, max_working_hours)
        self.companies[company_name] = company
        return f"{company_name} has been added successfully."

    def calculate_wages_for_company(self, company_name):
        """
        Description:
            Calculates the wages for a specific company.

        Parameters:
            company_name : str  Name of the company.
        
        Returns:
            str: Company summary after wage calculation.
        """
        if company_name not in self.companies:
            return f"Company {company_name} not found."

        company = self.companies[company_name]
        company.calculate_wage()
        return company.get_company_summary()

    def show_companies(self):
        """
        Description:
            Shows the details of all companies.
        Parameters:
            None
        Returns:
            str: Summary of all companies.
        """
        if not self.companies:
            return "No companies have been added yet."

        summary = "Summary of all companies:\n"
        for company in self.companies.values():
            summary += company.get_company_summary() + "\n"
        return summary

def main():
    manager = EmpWageManager()

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Calculate wages for a company")
        print("3. Show company wages")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
            working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
            max_working_hours = int(input(f"Enter the maximum working hours for {company_name}: "))
            
            result = manager.add_company(company_name, wage_per_hour, working_days, max_working_hours)
            print(result)

        elif choice == "2":
            company_name = input("Enter the company name: ")
            
            result = manager.calculate_wages_for_company(company_name)
            print(result)

        elif choice == "3":
            result = manager.show_companies()
            print(result)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
