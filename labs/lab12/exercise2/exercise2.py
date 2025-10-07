score = float(input())
score_count = 0
total_score = 0.0
average_score = 0.0

while score >=0 and score<=100 :
    score_count +=1
    total_score += score
    score = float(input())

if score_count > 0:
    average_score = total_score / score_count
    
print(score_count)
print(total_score)
print(f"{average_score:.2f}")
