#wapp to check the given leap year or not 

n=float(input("enter the year"))

match n%4:
	case 0 :	print("is a leap year")
	case _ :	print("not a leap year")
