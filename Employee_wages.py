'''

@Author:Vijay Kumar M N
@Date: 2024-08-19
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-19
@Title : python program to Ability to manage Employee Wage of multiple companies

'''
import random

class CompanyEmpWage:
    def __init__(self, company_name, wage_per_hour, working_days, max_working_hours):
        
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.working_days = working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0
        self.total_working_hours = 0
        self.daily_wages = {}
        self.employees = []

    def check_employee(self):
        """
        Description:
            Determines the daily hours and status of an employee.

        Parameters:
            None
        Returns:
            tuple: (daily_hours, status) - Number of hours worked in a day and attendance status.
        """
        status = random.randint(0, 1)  
        if status == 1:
            check_time = random.randint(0, 1) 
            if check_time == 0:
                daily_hours = 8
            else:
                daily_hours = 4
        else:
            daily_hours = 0
        
        return daily_hours, status

    def calculate_wages(self):
        """
        Description:
            Tracks the daily attendance of employees and updates working hours and wages.

        Parameters:
            None
        
        Returns:
            None
        """
        day = 1
        while day <= self.working_days and self.total_working_hours < self.max_working_hours:
            daily_hours, status = self.check_employee()
            if self.total_working_hours + daily_hours > self.max_working_hours:
                daily_hours = self.max_working_hours - self.total_working_hours
            daily_wage = daily_hours * self.wage_per_hour
            self.daily_wages[f"Day {day}"] = daily_wage
            self.total_wage += daily_wage
            self.total_working_hours += daily_hours
            day += 1

    def get_employee_summary(self, emp_name):
        """
        Description:
            Returns a summary for the employee's wages.

        Parameters:
            emp_name : str  Name of the employee.

        Returns:
            str: Summary of the employee's wage, working hours, and daily wages.
        """
        summary = f"Employee: {emp_name}, Total Working Hours: {self.total_working_hours}, Total Wage: {self.total_wage}\n"
        summary += "Daily Wages:\n"
        summary += "{\n"
        for day, wage in self.daily_wages.items():
            summary += f"  {day}: {wage}\n"
        summary += "}\n"
        return summary

    def add_employee(self, emp_name):
        """
        Description:
            Adds an employee to the company's employee list and calculates their wages.

        Parameters:
            emp_name : str  Name of the employee.

        Retruns:
            None
        """
        self.calculate_wages()
        employee_details = {
            'name': emp_name,
            'total_wage': self.total_wage,
            'total_working_hours': self.total_working_hours,
            'daily_wages': self.daily_wages
        }
        self.employees.append(employee_details)

class EmpWageBuilder:
    def __init__(self):
        self.companies = []

    def add_company(self, company_name, wage_per_hour, working_days, max_working_hours):
        """
        Description:
            Adds a new company to the builder.

        Parameters:
            company_name : str  Name of the company.
            wage_per_hour : int  Wage per hour for the company.
            working_days : int  Number of working days in a month for the company.
            max_working_hours : int  Maximum working hours in a month.
        Returns:
            Company
        """
        company = CompanyEmpWage(company_name, wage_per_hour, working_days, max_working_hours)
        self.companies.append(company)
        return company

    def calculate_wages_for_company(self, company, emp_name):
        """
        Description:
            Calculates the wages for an employee in a specific company.

        Parameters:
            company : CompanyEmpWage  The company object.
            emp_name : str  Name of the employee.

        Returns:
            str: Employee summary after wage calculation.
        """
        company.add_employee(emp_name)
        return company.get_employee_summary(emp_name)

    def show_companies(self):
        """
        Description:
            Shows the details of all companies and their employees' wages.

        Parameters:
            None
        Returns:
            str: Summary of all companies and their employees.
        """
        if not self.companies:
            return "No companies have been added yet."

        summary = "Summary of all companies:\n"
        for company in self.companies:
            summary += f"\nCompany: {company.company_name}\n"
            summary += f"Wage per Hour: {company.wage_per_hour}, Working Days per Month: {company.working_days}, Max Working Hours: {company.max_working_hours}\n"
            if not company.employees:
                summary += "No employees in this company.\n"
            else:
                for emp in company.employees:
                    summary += company.get_employee_summary(emp['name'])
        return summary

def main():
    builder = EmpWageBuilder()

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Add an employee and calculate wages")
        print("3. Show company wages")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
            working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
            max_working_hours = int(input(f"Enter the maximum working hours in a month for {company_name}: "))
            
            builder.add_company(company_name, wage_per_hour, working_days, max_working_hours)
            print(f"Company {company_name} added successfully.")

        elif choice == "2":
            company_name = input("Enter the company name to add an employee: ")
            company = next((c for c in builder.companies if c.company_name == company_name), None)
            if not company:
                print(f"Company {company_name} does not exist.")
            else:
                emp_name = input("Enter the employee's name: ")
                result = builder.calculate_wages_for_company(company, emp_name)
                print(result)
                

        elif choice == "3":
            result = builder.show_companies()
            print(result)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


