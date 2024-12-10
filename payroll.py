class Employ:
    def __init__(self, hourly_rate, hourly_work, bonus_percentage=0, tax_rate=0):
        self.hourly_rate = hourly_rate
        self.hourly_work = hourly_work
        self.bonus_percentage = bonus_percentage
        self.tax_rate = tax_rate
        
    def calculate_basic_salary(self):
        return self.hourly_rate * self.hourly_work
    
    def calculate_overtime_pay(self):
        regular_hour = 40
        overtime_rate = 1.5 * self.hourly_rate
        if self.hourly_work > regular_hour:
            overtime_hours = self.hourly_work - regular_hour
            overtime_pay = overtime_hours * overtime_rate
            return overtime_pay
        else:
            return 0
    
    def calculate_bonus(self, basic_salary):
        return basic_salary * (self.bonus_percentage / 100)
    
    def calculate_tax_deduction(self, basic_salary):
        return basic_salary * (self.tax_rate / 100)
    
    def calculate_total_pay(self):
        basic_salary = self.calculate_basic_salary()
        overtime_pay = self.calculate_overtime_pay()
        bonus_percentage = self.calculate_bonus(basic_salary)
        tax_deduction = self.calculate_tax_deduction(basic_salary)
        total_pay = basic_salary + bonus_percentage + overtime_pay - tax_deduction
        return total_pay, basic_salary, overtime_pay, bonus_percentage, tax_deduction
    
    def month(self):
        week_salary = self.calculate_basic_salary()
        return week_salary * 4  

hourly_rate = float(input("Enter your hourly rate: "))
hourly_work = float(input("Enter your number of work hours in a week: "))
bonus_percentage = float(input("Enter your bonus percentage: "))
tax_rate = float(input("Enter your tax rate: "))

employee = Employ(hourly_rate, hourly_work, bonus_percentage, tax_rate)

total_pay, basic_salary, overtime_pay, bonus, tax_deduction = employee.calculate_total_pay()

print(f"Basic Salary: ${basic_salary:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Bonus: ${bonus:.2f}")
print(f"Tax Deduction: ${tax_deduction:.2f}")
print(f"Total Pay: ${total_pay:.2f}")

monthly_salary = employee.month()
print(f"Monthly Salary: ${monthly_salary:.2f}")
