#faulty Calculater

n1 =int(input("Enter the first number\n"))

print("choose option to calculate\nEnter + to add\nEnter - to subtraction\nEnter * to multiplaction\nEnter / to division")


operator = input()

n2 = int(input("Enter the second number\n"))

if n1==45 and operator=="*" and n2==3:
	print("Answer is 145")
	
elif n1==56 and n2==9 and operator=="+":
	print("Answer is 77")
	
elif n1==56 and n2==6 and operator=="/":
	print("Answer is 4")
	
elif operator=="+":
	print("Answer is",n1+n2)
	
elif operator=="-":
	print("Answer is", n1-n2)
	
elif operator=="*":
	print("Answer is",n1*n2)
	
elif operator=="/":
	print("Answer is",n1/n2)