#wapp to read rating from 1 to 5

r=int(input("enter the rating from 1 to 5 -"))

if (r<1) or (r>5):
	print("invalid")
elif (r==5) or (r==4):
	print("excellent")
elif (r==3) or (r==2):
	print("ok")
else:
	print("poor")