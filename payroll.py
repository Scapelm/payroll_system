class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method.")

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission

if __name__ == "__main__":
    employees = [
        SalaryEmployee(1, "Alice", 1200),
        HourlyEmployee(2, "Bob", 40, 20),
        CommissionEmployee(3, "Charlie", 1000, 250)
    ]

    print("Payroll Report\n==============")
    for emp in employees:
        print(f"Employee: {emp.name} (ID: {emp.emp_id})")
        print(f"Pay: ${emp.calculate_payroll():.2f}\n")