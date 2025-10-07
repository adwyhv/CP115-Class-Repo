current_reading = int(input())
previous_reading = int(input())
consumption= current_reading-previous_reading
water_cost=0
total_bill=0

if consumption<=20 :
    water_cost = consumption * 0.57
elif consumption<=35 :
    water_cost = (20*0.57)+((consumption-20) * 1.03)
elif consumption > 35 :
    water_cost = (20*0.57)+(15*1.03)+((consumption-35)*1.40)

total_bill = water_cost + 10


print(consumption)
print(water_cost)
print(total_bill)