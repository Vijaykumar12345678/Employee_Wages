'''

@Author:Vijay Kumar M N
@Date: 2024-08-4
@Last Modified by: Vijay Kumar M N
@Last Modified: 2024-08-14
@Title : python program to compute Compute Employee Wage for multiple companies

'''
import random

class EmpWageBuilder:
    WAGE_PER_HOUR = 0
    FULL_TIME = 8
    PART_TIME = 4
    MONTH_WORKING_DAYS = 0
    MAXIMUM_WORKING_HOURS = 100
    
    
    @classmethod
    def check_employee(cls):
        """
        Description:
            This function checks if the employee is present and returns their status.

        Returns:
            full-time Present : string If the employee is present full-time
            part-time Present : string If the employee is present part-time
            Absent: string If the employee is absent
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
    
    @classmethod
    def calculate_wages_for_month(cls):
        """
        Description:
            This function calculates the total monthly wage by checking each day whether the employee is present and whether they worked full-time or part-time.

        Returns:
            total_wage : int Monthly wage
            daily_wages : dict Daily wages with details
            tot_working_hours : int Total working hours
            tot_working_days : int Total working days
        """
        total_wage = 0
        daily_wages = {}
        tot_working_hours, tot_working_days = 0, 0
        
        while tot_working_hours < cls.MAXIMUM_WORKING_HOURS and tot_working_days < cls.MONTH_WORKING_DAYS:
            status = cls.check_employee()
            daily_wages[f"Day_{tot_working_days + 1}"] = {
                'status': status,
                'hours_worked': 0,
                'daily_wage': 0
            }
            
            if status != "Absent":
                if status == "full-time Present":
                    hours = cls.FULL_TIME
                else:
                    hours = cls.PART_TIME
                
                daily_wages[f"Day_{tot_working_days + 1}"]['hours_worked'] = hours
                daily_wages[f"Day_{tot_working_days + 1}"]['daily_wage'] = cls.WAGE_PER_HOUR * hours
                tot_working_hours += hours
                total_wage += cls.WAGE_PER_HOUR * hours
            tot_working_days += 1

        return total_wage, daily_wages, tot_working_hours, tot_working_days


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
        str Summary of the company's working hours and total wage.
    """
    if company_name in companies:
        return f"The company name {company_name} is already present."
    
    EmpWageBuilder.WAGE_PER_HOUR = wage_per_hour
    EmpWageBuilder.MONTH_WORKING_DAYS = working_days

    total_wage, daily_wages, total_working_hours, total_working_days = EmpWageBuilder.calculate_wages_for_month()
    
    companies[company_name] = {
        'total_wage': total_wage,
        'daily_wages': daily_wages,
        'total_working_hours': total_working_hours,
        'total_working_days': total_working_days
    }
    
    return f"{company_name} - Total Working Hours: {total_working_hours}, Total Wage: {total_wage}"


def display_companies(companies):
    """
    Description:
        Displays the summary of all companies and their wage details, including daily wages.
    
    Parameters:
        companies : dict Dictionary of companies and their wage details.
    
    Returns:
        str Summary of all companies.
    """
    if not companies:
        return "No companies have been added yet."
    
    summary = "Summary of all companies:\n"
    for company, details in companies.items():
        summary += f"\n{company} - Total Working Hours: {details['total_working_hours']}, Total Wage: {details['total_wage']}\n"
        summary += "  Daily Wages:\n"
        
        for day, wage_info in details['daily_wages'].items():
            summary += f"    {day}: Status: {wage_info['status']}, Hours Worked: {wage_info['hours_worked']}, Daily Wage: {wage_info['daily_wage']}\n"
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


