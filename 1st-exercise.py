import random
user = int(input("Select number :\n 1 for Stone\n 2 for Paper\n 3 for Scissor \n > "))
comp = random.randint(1, 3)

def check(comp, user):
  if comp == user:
    return 0
  elif comp == 2 and user == 1:
    return -1
  elif comp == 3 and user == 2:
    return -1
  elif comp == 1 and user == 3:
    return -1
  else:
    return 1
score = check(comp, user)
print("You choose : ",user)
print("The computer choose : ",comp)
if(score == 0):
  print("Its a Draw")
elif(score == 1):
  print("You won")
elif(score == -1):
  print("You lost")
