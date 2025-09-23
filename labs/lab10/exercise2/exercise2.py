age = int(input())
accident_count = int(input())

if age < 25 :
    base_premium = 2400
elif 25<= age <=50 :
    base_premium = 1800
else :
    base_premium =2000

if accident_count == 0:
    penalty = 0
    discount_amount = base_premium * 0.1
    
elif accident_count <= 2:
    penalty = 300
    discount_amount = 0
    
else:
    penalty = 600
    discount_amount = 0

final_premium = base_premium + penalty - discount_amount

base_premium = int(base_premium)
final_premium = int(final_premium)
discount_amount = int(discount_amount)

print(base_premium)
print(final_premium)
print(discount_amount)