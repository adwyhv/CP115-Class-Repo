employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = overtime_hours * 35
gross_income = overtime_pay + base_salary
epf_deduction = 11 / 100
socso_deduction = 0.5 / 100

if tax_status == "Single" and gross_income>=5000:
    tax_rate = 0.22
elif tax_status == "Single" and gross_income<=5000:
    tax_rate = 0.18
elif tax_status == "Married" and gross_income>=6000:
    tax_rate = 0.20
elif tax_status == "Married" and gross_income<=6000:
    tax_rate = 0.15
elif tax_status == "Head" and gross_income>=5500:
    tax_rate=0.25
elif tax_status == "Head" and gross_income<=5500:
    tax_rate = 0.19

net_salary = gross_income * (1 - (epf_deduction + socso_deduction)) * (1 - tax_rate)
tax_rate = tax_rate*100




print(employee_name)
print(f"{tax_rate:.0f}%")
print(f"{net_salary:.2f}")