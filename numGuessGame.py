n= 19

attempt=0
while(attempt<5):
	print("Guess the value of n by enter any number between 14 to 20 :")
	temp=int(input())
	attempt=attempt+1
	if(temp==n):
		print("Congratulation! YOU WIN..")
		break
	elif(attempt<5):
		print("Oops! Try again..")
		continue
	
print("Your Total Attempt =",attempt)

if(attempt==5):
		print("GAME OVER")