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

#Checking if a number can be presented as a sum of two prime numbers
def get_sum_of_primes(num):
	primes=[]
	for x in range(2,int(num/2)+1):
		if is_prime1(x) and is_prime1(num-x):
			primes.append(str(num)+" = "+ str(x)+ " + "+str(num-x))
	return primes

n1=29
n2=34
print(is_prime1(n1))
print(is_prime2(n1))
print(get_sum_of_primes(n2))
