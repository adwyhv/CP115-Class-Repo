score_input = input()
passing_count = 0
failing_count = 0
pass_rate = 0

while score_input != "end" :
    if int(score_input)>= 60:
        passing_count +=1
    else:
        failing_count +=1
    score_input = input()

if passing_count+failing_count >0:
    pass_rate = (passing_count /(passing_count+failing_count) ) * 100




print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
