Creating a Simple Payroll System
The HR system needs to process payroll for the company's employees, but there are different types of
employees depending on how their payroll is calculated.
(0
Implement a base class Employee that handles the common interface for every employee type.
Employee is the base class for all employee types. It is constructed with an empjd and a name je
every Employee must have an id assigned as well as a name.
The HR system requires that every Employee processed must have a çcalculate_payroll) method
that returns the weekly salary for the employee. The implementation of that interface differs
depending on the type of Employee.
(ii)
Create a derived class called SalaryEmployee that inherits Employee. The class is initialized with
the empjid and name required by the base class, use super() to inherit the members of the base
class.
SalaryEmployes also requires a weekly_salary initialization parameter that represents the amount
the employee makes per week. The class provides the required çalculate payroll) method used by
the HR system. The implementation just returns the amount stored in weekly_salary.
(ii)
The company also employs manufacturing workers that are paid by the hour, so you add an
HourlyEmployee to the HR system: The HourlyEmployee class is initialized with emp jd and name,
like the base class, plus the hours worked and the hourly rate required to calculate the payrol.
The calculate_payrolLỌ method is implemented by returning the hours worked times the hour rate.
Finally, the company employs sales associates that are paid through a fixed salary plus a
(iv)
commission based on their sales, so you create a CommissionEmployee class: Create a class
called ÇommissionEmployee that inherits from SalarEmployee because both classes have a
weekly salary to consider. At the same time, CommissionEmployee is initialized with a
commission value that is based on the sales for the employee. The calculate_payrall0 leverages the
implementation of the base class to retrieve the fixed salary and adds the commission value.
Since CommissionEmployee derives from SalaryEmployee, you have access to the weeklysalary
property directly, and you could've implemented calculatepayroll0 using the value of that
property.
Write a python program to implement the above
￼Enter
