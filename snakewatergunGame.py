#Snake  water  gun  Game

print("Type Your Name : ")
nam=input()

print(f"\n\nHi ! {nam} Let's Play snake water gun game...")

import random
computer=["s","w","g"]

round=0
user_point=0
computer_point=0

while(round<10):
	round=round+1
	print("\n\nRound ",round)
	user_input=input("s for snake\n w for water \n g for gun\n")
	randam=random.choice(computer)
	
	
	if (user_input=="s" and randam=="w"):
		user_point=user_point+1
		print(f"your guess {user_input} and computer guess is {randam} \n{nam} won 1 point\npoint of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input=="s" and randam=="g"):
		computer_point=computer_point+1
		print(f"your guess {user_input} and computer guess is {randam} \nComputer won 1 point\npoint of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input=="w" and randam=="s"):
		computer_point=computer_point+1
		print(f"your guess {user_input} and computer guess is {randam} \nComputer won 1 point\npoint of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input=="w" and randam=="g"):
		user_point=user_point+1
		print(f"your guess {user_input} and computer guess is {randam} \n{nam} won 1 point\npoint of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input=="g" and randam=="w"):
		computer_point=computer_point+1
		print(f"your guess {user_input} and computer guess is {randam} \nComputer won 1 point\npoint of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input=="g" and randam=="s"):
		user_point=user_point+1
		print(f"your guess {user_input} and computer guess is {randam} \n{nam} won 1 point\n point of {nam} =",user_point)
		print("point of computer =",computer_point)
		
	elif (user_input==randam):
		print(f"your guess {user_input} and computer guess is {randam} \nRound {round} Tie \n point of {nam} =",user_point)
		print("point of computer =",computer_point)
	else:
		print("you have input wrong \n")
		
print("Game Over!")

if (user_point<computer_point):
	print(f"{nam} Loss\n Computer Won")
elif(user_point>computer_point):
		print(f"{nam} Won\n Computer Loss")
		
else:
	print("Game Tie ! No One win to each...")