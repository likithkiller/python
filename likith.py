import random
while True:
	    r  = input("\npress r to roll\n press q to quit\n")
	    if r =="r":
	    	print("you got :",random.randint(1,6))
	    elif r =="q":
	    	print("bye")
	    	exit()
