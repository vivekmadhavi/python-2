#wapp to read rating from 1 to 5 and print msg
#5/4 ->excellent  3/2 ->ok

r=int(input("enter the rating from 1 to 5 -"))

match r :
	case 5|4:	print("excellent")
	case 3|2:	print("ok")
	case 1 :	print("poor")
	case _ :	print("invalid")