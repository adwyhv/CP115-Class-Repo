main_dish = 25
appetizer=12
drink=8
bill= (main_dish*3)+(appetizer*2)+(4*drink)
serviceTax=0.1 * bill
deliveryFee=5
totalBill= (bill+serviceTax+deliveryFee)
bill_per_person=totalBill//6
print(bill_per_person)