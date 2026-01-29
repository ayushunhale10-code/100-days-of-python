target=int(input("Enter a number between 0 and 1000: "))
total=0
for i in (range(0,target+1,2)):#target+1 as it will not take the target value so +1
   total+=i
print(total)
