day_type = input()
show_time = int(input())
customer_type = input()
is_student = input()
evening_show= 3

if day_type == "Weekday" and show_time > 18 and is_student == "Yes" and customer_type == "Adult":
    base_price = 15 + 3
    final_price = base_price * 0.9
elif day_type == "Weekday" and show_time >18 and is_student == "Yes" and customer_type == "Child":
    base_price = 10 + 3
    final_price =base_price *0.9
elif day_type == "Weekday" and show_time >18 and is_student == "Yes" and customer_type =="Senior":
    base_price = 12 + 3
    final_price = base_price*0.9
elif day_type == "Weekday" and show_time < 18 and is_student == "Yes" and customer_type =="Adult":
    base_price = 15
    final_price = base_price * 0.9
elif day_type == "Weekday" and show_time < 18 and is_student == "Yes" and customer_type =="Child":
    base_price =10
    final_price = base_price*0.9
elif day_type == "Weekday" and show_time < 18 and is_student =="Yes" and customer_type == "Customer":
   base_price = 12
   final_price = base_price * 0.9


if day_type == "Weekday" and show_time >18 and is_student == "No" and customer_type == "Adult":
    base_price = 15 + 3
    final_price = base_price
elif day_type =="Weekday" and show_time > 18 and is_student =="No" and customer_type == "Child":
   base_price = 10 + 3
   final_price = base_price
elif day_type == "Weekday" and show_time > 18 and is_student =="No" and customer_type == "Senior":
    base_price = 12 + 3
    final_price = base_price

if day_type == "Weekday" and show_time <18 and is_student == "No" and customer_type == "Adult":
    base_price = 15
    final_price = base_price
elif day_type =="Weekday" and show_time < 18 and is_student =="No" and customer_type == "Child":
   base_price = 10 
   final_price = base_price
elif day_type == "Weekday" and show_time < 18 and is_student =="No" and customer_type == "Senior":
   base_price = 12
   final_price = base_price


if day_type == "Weekend" and show_time >18 and is_student=="No" and customer_type =="Adult":
   base_price = 18 + 3
   final_price = base_price
elif day_type == "Weekend" and show_time >18 and is_student=="No" and customer_type =="Child":
   base_price = 12 + 3
   final_price = base_price
elif day_type == "Weekend" and show_time >18 and is_student=="No" and customer_type=="Senior":
   base_price = 15 + 3
   final_price = base_price

if day_type == "Weekend" and show_time <18 and is_student=="No" and customer_type =="Adult":
    base_price = 18 
    final_price = base_price
elif day_type == "Weekend" and show_time <18 and is_student=="No" and customer_type =="Child":
   base_price = 12 
   final_price = base_price
elif day_type == "Weekend" and show_time <18 and is_student=="No" and customer_type=="Senior":
   base_price = 15 
   final_price = base_price


print(base_price)
print(final_price)