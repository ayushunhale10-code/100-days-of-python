rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random
game=[rock,paper,scissors]#list
choice=int(input("type your choice for ROCK it is 0 for PAPER it is 1 for SCISSORS 2"))#input from the user
your_choice=game[choice]
print(your_choice)
random_choice=random.randint(0,2)
computer_choice=game[random_choice]
print(computer_choice)
list_of_current_choices=[your_choice,computer_choice]
list_of_situation=[[rock,paper],[paper,scissors],[scissors,rock],[paper,rock],[scissors,paper],[rock,scissors]]
win="you win"
lose="you lose"
if choice==random_choice:
    print("its a tie")
elif list_of_current_choices==list_of_situation[0]:
    print(lose)
elif list_of_current_choices==list_of_situation[1]:
    print(lose)
elif list_of_current_choices==list_of_situation[2]:
    print(lose)
elif list_of_current_choices==list_of_situation[3]:
    print(win)
elif list_of_current_choices==list_of_situation[4]:
    print(win)
elif list_of_current_choices==list_of_situation[5]:
    print(win)

