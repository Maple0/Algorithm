#Author: Maple0
#Github:https://github.com/Maple0
#19th Aug 2016

# Given two strings: string A and string B , assume the length of string B is less than string A.
# write a algorithm to check if string A contains string B
#For example:  string A is "A","B","C","D" and string B is "B","C","D"  then the string A contains the string B

import hashlib
# time complexity is bad O(n*m)
def contains_solution1(string_a,string_b):
	for b in string_b:
		isContained = False
		for a in string_a:
			if b == a:
				isContained=True
				break
		if isContained==False:
			return False
	return True

# time complexity is good O(m+n) but the risk is potential overflow of prime product
def contains_solution2(string_a,string_b):
	p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,61, 67, 71, 73, 79, 83, 89, 97, 101]
	f= 1;
	for a in string_a:
		x=  p[ord(a) - ord('A')]
		if f % x:
			f *= x;

	for b in string_b:
		x=p[ord(b) - ord('A')]
		if f % x:
			return False
	return True

# accepted algorithm with reasonable  time complexity O(m+n) 
def contains_solution3(string_a,string_b):
	hashVal=0
	for a in string_a:
		hashVal|= 1 << (ord(a)- ord('A'))
	print(hashVal)
	for b in string_b:
	 	if hashVal & (1 << (ord(b)- ord('A')))==0:
	 		return False
	return True


stringA=["A","B","C","D"]
stringB=["B","A","D"]
print(contains_solution1(stringA,stringB))
print(contains_solution2(stringA,stringB))
print(contains_solution3(stringA,stringB))
			