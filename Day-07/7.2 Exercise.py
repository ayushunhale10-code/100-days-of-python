import random

word_list=["ardvark","baboon","camel"]
choice=random.choice(word_list)
guess=input("Enter your guess: ").lower()
display=[]
for choices in choice:
    if choices==guess:
        display.append(choices)
    else:
        display.append("_")

print(display)
