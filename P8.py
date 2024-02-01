#wapp to read rating from 1 to 5

r=int(input("enter the rating from 1 to 5 -"))

match r :
	case 5:	print("excellent")
	case 4:	print("excellent")
	case 3:	print("ok")
	case 2:	print("ok")
	case 1:	print("poor")
	case _:	print("invalid")
	