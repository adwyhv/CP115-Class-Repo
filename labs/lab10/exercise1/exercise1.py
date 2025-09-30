position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18


overtime_pay = 0
if overtime_hours > 0 :
    overtime_pay = overtime_hours * hourly_rate * 1.5
    if is_weekend == "Yes":
            overtime_pay = overtime_pay +(overtime_hours * 5)

total_pay = overtime_pay


# Calculate overtime pay (1.5x base rate)
overtime_rate = hourly_rate * 1.5
overtime_pay = overtime_hours * overtime_rate

# Add weekend bonus if applicable
if is_weekend.lower() == "yes":
    weekend_bonus = overtime_hours * 6
    overtime_pay += weekend_bonus

# Total pay is same as overtime pay
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)