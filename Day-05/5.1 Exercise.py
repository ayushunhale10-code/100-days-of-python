student_heights=input("enter student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total=0
for i in student_heights:
    total+=i
print(f"total height is {total}")
ranges=(len(student_heights))
print(f"No of student is  {ranges}")
avg_height=int(total/ranges)
print(f"average height is {avg_height}")

