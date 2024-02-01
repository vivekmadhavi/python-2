#wapp to ask the age of the use and print if the user can vote


age = float(input("enter the age"))

if (age<0) or (age>100):
	print("invalid")
elif  age >= 18 :
	print("you can vote")
else:
	print("not possible")