import random

word_list=["ardvark","baboon","camel"]
choice=random.choice(word_list)
guess=input("Enter your guess: ").lower()
for i in choice:
    if guess==i:
        print("right")
    else:
        print("wrong")