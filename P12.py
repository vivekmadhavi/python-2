#wapp to chck the given integer is even or odd

n=float(input("enter the number"))

match n%2:
	case 0 :	print("even number")
	case _ :	print("odd number")