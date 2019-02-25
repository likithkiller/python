import random
#this is a dictionary
d = {8:67,9:45,4:80,5:44,1:90,6:56,3:88,2:78}

p = random.choice([3,8,9,5,1,6,2])

print("you got" ,p)

if p in d:
	if p > d[p]:
		print("snake")
	else:
		print("ladder")
print("you can go to",d[p]) 

