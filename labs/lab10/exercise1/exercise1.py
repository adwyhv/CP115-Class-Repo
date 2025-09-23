position = input()
overtime_hours = int(input())
is_weekend = input()

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


print(hourly_rate)
print(overtime_pay)
print(total_pay)