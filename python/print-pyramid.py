#Author: Maple0
#Github:https://github.com/Maple0
#1st Sep 2016
#print pyramid by using *

def print_pyramid1(rows):
	for x in range(0,rows):
		print("*"*(x+1))

def print_pyramid2(rows):
	i=rows
	while i>0:
		print("*"*i)
		i-=1

def print_pyramid3(rows):
	for i in range(0,rows):
		print(' '*(rows-i-1) + '*' * (2*i+1))
rows=10
#print_pyramid1(rows)
#print_pyramid2(rows)
print_pyramid3(rows)