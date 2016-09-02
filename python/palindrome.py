#Author: Maple0
#Github:https://github.com/Maple0
#1st Sep 2016
#Checking whether a number is palindrome or not 
import datetime
def is_palindrome1(num):
	remainder=reverse=0
	temp=int(num)
	while(temp!=0):
		remainder=temp%10
		reverse=reverse*10+remainder
		temp=int(temp/10)
	return reverse==num

#better performance
def is_palindrome2(num):
	temp =str(num)
	start=0
	end=len(temp)-1
	while start < end:
		if temp[start] != temp[end]:
			return False
		start+=1
		end-=1
	return True

num1=12345678987654321
num2=76152

print(is_palindrome1(num1))
print(is_palindrome1(num2))

print(is_palindrome2(num1))
print(is_palindrome2(num2))



