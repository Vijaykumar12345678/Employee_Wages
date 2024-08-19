"""
@Author:Vijay Kumar M N
@Date: 2024-08-17
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-17
@Title : python program to manage Employee Wage of multiple companies
"""
import random

class Employee:
    def __init__(self, employee_id, employee_name):
        """
        Description:
        Initializes an Employee object with an ID and a name.
        Parameters:
        employee_id : integer The ID of the employee.
        employee_name : string The name of the employee.
        Returns:
        None
        """
        self.employee_id = employee_id
        self.employee_name = employee_name

    def __str__(self):
        """
        Description:
        Provides a string representation of the Employee object.
        Returns:
        string: A string describing the employee ID and name.
        """
        return f"ID: {self.employee_id}, Name: {self.employee_name}"

class CompanyEmpWage:
    def __init__(self, company_name, wage_per_hour, working_days):
        """
        Description:
        Initializes a CompanyEmpWage object with company details and initializes
        an employee list and total wage counter.
        Parameters:
        company_name : int The name of the company.
        wage_per_hour : int The wage per hour for the company's employees.
        working_days : int The total number of working days in a month.
        Returns:
        None
        """
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.working_days = working_days
        self.total_wage = 0
        self.employees = []
        self.employee_id_counter = 1  # To start employee IDs from 1 for each company

    def add_employee(self, employee_name):
        """
        Description:
        Adds a new employee to the company’s employee list.
        Parameters:
        employee_name : string The name of the employee to be added.
        Returns:
        Employee: The Employee object that was added.
        """
        employee = Employee(self.employee_id_counter, employee_name)
        self.employees.append(employee)
        self.employee_id_counter += 1
        return employee

    def remove_employee_by_id(self, employee_id):
        """
        Description:
        Removes an employee from the company's employee list by their ID.
        Parameters:
        employee_id : int The ID of the employee to be removed.
        Returns:
        None
        """
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def __str__(self):
        """
        Description:
        Provides a string representation of the CompanyEmpWage object,
        including the company’s total wage, working days, wage per hour,
        and a list of employees.
        Returns:
        str: A string describing the company’s details and its employees.
        """
        employees_str = ', '.join([str(emp) for emp in self.employees])
        return (f"{self.company_name} - Total Wage: {self.total_wage}, Working Days: {self.working_days}, "
                f"Wage Per Hour: {self.wage_per_hour}\nEmployees: {employees_str}")

class EmpWageBuilder:
    def __init__(self):
        """
        Description:
        Initializes an EmpWageBuilder object, which manages a list of CompanyEmpWage objects.
        Returns:
        None
        """
        self.company_emp_wage_list = []

    def add_company_emp_wage(self, company_name, wage_per_hour, working_days):
        """
        Description:
        Adds a new company to the list of managed companies.
        Parameters:
        company_name : string The name of the company.
        wage_per_hour : int  The wage per hour for the company's employees.
        working_days : int The number of working days in a month for the company.
        Returns:
        None
        """
        company_emp_wage = CompanyEmpWage(company_name, wage_per_hour, working_days)
        self.company_emp_wage_list.append(company_emp_wage)

    def remove_company(self, company_name):
        """
        Description:
        Removes a company from the list by its name.
        Parameters:
        company_name : string The name of the company to be removed.
        Returns:
        None
        """
        self.company_emp_wage_list = [company for company in self.company_emp_wage_list if company.company_name != company_name]

    def update_company(self, company_name, wage_per_hour=None, working_days=None):
        """
        Description:
        Updates the details of an existing company.
        Parameters:
        company_name : string The name of the company to be updated.
        wage_per_hour : int The new wage per hour (if provided).
        working_days : int The new number of working days (if provided).
        Returns:
        bool: True if the company was updated, False if the company was not found.
        """
        for company in self.company_emp_wage_list:
            if company.company_name == company_name:
                if wage_per_hour:
                    company.wage_per_hour = wage_per_hour
                if working_days:
                    company.working_days = working_days
                return True
        return False

    def add_employee_to_company(self, company_name, employee_name):
        """
        Description:
        Adds a new employee to a specific company.
        Parameters:
        company_name : string The name of the company.
        employee_name : string The name of the employee to be added.
        Returns:
        Employee: The Employee object if the company was found and the employee was added, otherwise None.
        """
        for company in self.company_emp_wage_list:
            if company.company_name == company_name:
                return company.add_employee(employee_name)
        return None

    def remove_employee_from_company(self, company_name, employee_id):
        """
        Description:
        Removes an employee from a specific company by their ID.
        Parameters:
        company_name : string The name of the company.
        employee_id : int The ID of the employee to be removed.
        Returns:
        bool: True if the employee was removed, False if the company or employee was not found.
        """
        for company in self.company_emp_wage_list:
            if company.company_name == company_name:
                company.remove_employee_by_id(employee_id)
                return True
        return False

    def calculate_wage(self, company_emp_wage):
        """
        Description:
        Calculates the total wage and total working hours for a company’s employees based on their status (full-time or part-time).
        Parameters:
        company_emp_wage (CompanyEmpWage): The company object for which the wage is being calculated.
        Returns:
        None
        """
        total_working_hours = 0
        
        for day in range(company_emp_wage.working_days):
            status = random.choice(["full-time", "part-time"])
            
            if status == "full-time":
                daily_hours = 8
            else:  # part-time
                daily_hours = 4

            daily_wage = daily_hours * company_emp_wage.wage_per_hour
            company_emp_wage.total_wage += daily_wage
            total_working_hours += daily_hours
            
            print(f"Day {day + 1}: {status.capitalize()} - Hours Worked: {daily_hours}, Daily Wage: {daily_wage}")

        print(f"\n{company_emp_wage.company_name} - Total Working Hours: {total_working_hours}, Total Wage: {company_emp_wage.total_wage}\n")

    def calculate_wages_for_all(self):
        """
        Description:
        Calculates wages for all companies managed by EmpWageBuilder.
        Returns:        
        None
        """
        for company_emp_wage in self.company_emp_wage_list:
            self.calculate_wage(company_emp_wage)

    def show_company_wages(self):
        """
        Description:
        Displays the wage details for all companies.

        Returns:
        None
        """
        if not self.company_emp_wage_list:
            print("\nNo companies have been added yet.")
        else:
            print("\nSummary of all companies:")
            for company_emp_wage in self.company_emp_wage_list:
                print(company_emp_wage)

def main():
   
    emp_wage_builder = EmpWageBuilder()

    while True:
        print("\nOptions:")
        print("1. Add a company")
        print("2. Update a company")
        print("3. Delete a company")
        print("4. Add an employee to a company")
        print("5. Remove an employee from a company")
        print("6. Show company wages")
        print("7. Calculate wages for all companies")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            company_name = input("Enter the company name: ")
            wage_per_hour = int(input(f"Enter the wage per hour for {company_name}: "))
            working_days = int(input(f"Enter the number of working days in a month for {company_name}: "))
            emp_wage_builder.add_company_emp_wage(company_name, wage_per_hour, working_days)
            print(f"Company {company_name} added successfully.")

        elif choice == "2":
            company_name = input("Enter the company name to update: ")
            wage_per_hour = input("Enter new wage per hour (or press Enter to skip): ")
            working_days = input("Enter new number of working days (or press Enter to skip): ")
            updated = emp_wage_builder.update_company(company_name, wage_per_hour=int(wage_per_hour) if wage_per_hour else None, working_days=int(working_days) if working_days else None)
            if updated:
                print(f"Company {company_name} updated successfully.")
            else:
                print(f"Company {company_name} not found.")

        elif choice == "3":
            company_name = input("Enter the company name to delete: ")
            emp_wage_builder.remove_company(company_name)
            print(f"Company {company_name} deleted successfully.")

        elif choice == "4":
            company_name = input("Enter the company name: ")
            employee_name = input("Enter the employee name: ")
            employee = emp_wage_builder.add_employee_to_company(company_name, employee_name)
            if employee:
                print(f"Employee {employee_name} added to {company_name} with ID {employee.employee_id}.")
            else:
                print(f"Company {company_name} not found.")

        elif choice == "5":
            company_name = input("Enter the company name: ")
            employee_id = int(input("Enter the employee ID: "))
            if emp_wage_builder.remove_employee_from_company(company_name, employee_id):
                print(f"Employee with ID {employee_id} removed from {company_name}.")
            else:
                print(f"Company {company_name} or Employee with ID {employee_id} not found.")

        elif choice == "6":
            emp_wage_builder.show_company_wages()

        elif choice == "7":
            emp_wage_builder.calculate_wages_for_all()

        elif choice == "8":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
