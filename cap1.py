class Employee:
    def __init__(self, emp_name, yearly_income, job_title, num_of_children, cost_per_child):
        self.emp_name = emp_name
        self.yearly_income = yearly_income
        self.job_title = job_title
        self.num_of_children = num_of_children
        self.cost_per_child = cost_per_child
        
    def calculate_taxable_income(self):
        subtract = Deduction(self.yearly_income, self.job_title, self.num_of_children, self.cost_per_child)
        total_deduction = subtract.calculate_deductions()
        return self.yearly_income - total_deduction

class AnnualIncome(Employee):
    def calculate_annual_income(self):
        return self.yearly_income

class Deduction:
    def __init__(self, yearly_income, job_title, num_of_children, cost_per_child):
        self.yearly_income = yearly_income
        self.job_title = job_title
        self.num_of_children = num_of_children
        self.cost_per_child = cost_per_child

    def calculate_deductions(self):
        total_deduction = 0
        if self.job_title == "Regular":
            total_deduction += self.yearly_income 
            total_deduction += min(350000 * self.num_of_children, self.cost_per_child * self.num_of_children)
            total_deduction += 200
        elif self.job_title == "Temporary":
            total_deduction += 200
            total_deduction += min(350000 * self.num_of_children, self.cost_per_child * self.num_of_children)
        return total_deduction

class TaxCalculator:
    @staticmethod
    def calculate_tax(income):
        if income <= 300000:
            return 0
        elif 300001 <= income <= 400000:
            return income * 0.1
        elif 400001 <= income <= 650000:
            return income * 0.15
        elif 650001 <= income <= 1000000:
            return income * 0.2
        elif 1000001 <= income <= 1500000:
            return income * 0.25
        else:
            return income * 0.3

# Capture inputs
emp_name = input("Provide your full name : ")
yearly_income = float(input("Enter your yearly income : "))
job_title = input("Enter employee type (temporary/Regular): ").capitalize()
num_of_children = int(input('Enter Number of Children : '))
cost_per_child = int(input('Expenditure per child:'))

# Create Employee object and perform calculations
employee = Employee(emp_name, yearly_income, job_title, num_of_children, cost_per_child)
taxable_income = employee.calculate_taxable_income()

# Calculate deductions
deduction = Deduction(yearly_income, job_title, num_of_children, cost_per_child)
total_deduction = deduction.calculate_deductions()

# Display results on another screen
# Display results on another screen
print("\nResults:")
print(f"Employee Name: {emp_name}")
print(f"Annual Income: {employee.calculate_taxable_income()}")  # Corrected method call
print(f"Taxable Income: {taxable_income}")
print(f"Total Deduction Allowed: {total_deduction}")
print(f"Tax Liability: {TaxCalculator.calculate_tax(taxable_income)}")


if taxable_income < 300000:
    print(f"\n{emp_name}, Your Income is below taxable authority. You are exempted from paying tax.")
else:
    print(f"\n{emp_name}, you have taxable liability of Nu.", TaxCalculator.calculate_tax(taxable_income))
