student_scores=input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])

highest=student_scores[0]
for i in student_scores:
    if i>highest:
        highest=i
print("the highest score is ",highest)



