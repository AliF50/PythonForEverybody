score = raw_input("Enter Score: ")
score = float(score)
if(score >= 0.9):
    grade = 'A'
elif(score >= 0.8):
    grade = 'B'
elif(score >= 0.7):
    grade = 'C'
elif(score >= 0.6):
    grade = 'D'
elif(score >= 0):
    grade = 'F'
else:
    print('Score out of range, please enter a score within range.')
#quit();
print(grade)