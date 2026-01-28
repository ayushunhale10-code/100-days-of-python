line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]
map=[line1,line2,line3]
print("hiding your treasure! X marks the spot.")
position=input("enter the position of the treasure: ")
letter=position[0].lower()
#position[0] goes to the starting value
abc=["a","b","c"]
letter_index=abc.index(letter)
#.index used to find the position like for b it will return 1.
number_index=int(position[1])-1
#position-1 as the starting starts from 0.
map[number_index][letter_index]="X"
print(f"{line1}\n {line2}\n {line3}")
