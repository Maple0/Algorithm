#Author: Maple0
#Github:https://github.com/Maple0
#1st Sep 2016
#Checking whether a number is palindrome or not 

def is_palindrome(num):
	remainder=reverse=0
	temp=int(num)
	while(temp!=0):
		remainder=temp%10
		reverse=reverse*10+remainder
		temp=int(temp/10)
	return reverse==num

num1=12321
num2=76152
print(is_palindrome(num1))
print(is_palindrome(num2))