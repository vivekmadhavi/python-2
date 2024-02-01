#wapp to read rating from 1 to 5

r=int(input("enter the rating from 1 to 5 -"))

if r<1:
	print("invalid")
elif r>5:
	print("invalid")
elif r==5:
	print("excellent")
elif r==4:
	print("excellent")
elif r==3:
	print("ok")
elif r==2:
	print("ok")
else:
	print("poor")