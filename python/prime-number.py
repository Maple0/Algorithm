#Author: Maple0
#Github:https://github.com/Maple0
#1st Sep 2016
#Checking whether a number is prime or not 

def is_prime1(num):
	return num>1 and all(num % i for i in range(2, num))

def is_prime2(num):
	if num <=1:
		return False

	for x in range(2,int(num/2)+1):
		if num % x ==0:
			return False

	return True

n=11
print(is_prime1(n))
print(is_prime2(n))