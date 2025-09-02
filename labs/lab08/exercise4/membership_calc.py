base_membership=120
#each session rm80
personal_training=80.0
locker_rental=25
towel_service=15
#for new member,registration fee cost rm50 only for one-time
registration_fee=50
total_first_month=base_membership+personal_training+locker_rental+towel_service+registration_fee
print(total_first_month)
cost_after_1month=base_membership+personal_training+locker_rental+towel_service
print(cost_after_1month)
#kira cost for 12 month including first month
annual_cost= total_first_month + (11*cost_after_1month)
print(annual_cost)