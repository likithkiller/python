import random
#this is a dictionary
d = {8:67,9:45,4:80,5:44,1:90,6:56,8:88,2:78}

p = random.choice([3,4,5,43,52,56,22,68,31])

print("you got" ,p)

if p in d:
	if p> d[p]:
		print("snake")
    else:
		print("ladder") 

	print("you can go to",d[p]) 

