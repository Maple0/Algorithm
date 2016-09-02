#Author: Maple0
#Github:https://github.com/Maple0
#1st Sep 2016
#An implementation of fibonacci sequence in python

def generate_fibonacci(n):
	fibonacci=[0,1]
	i=0
	while i < n:
		next_fibonacci=fibonacci[i]+fibonacci[i+1]
		fibonacci.append(next_fibonacci)
		i+=1
	return fibonacci

fibonacci_numbers=generate_fibonacci(100)
print(fibonacci_numbers)