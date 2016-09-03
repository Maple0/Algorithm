#Author: Maple0
#Github:https://github.com/Maple0
#3st Sep 2016
#convert the decimal number into binary and vise-versa

def decimal_to_binary1(num):
	temp=int(num)
	remainder=0
	binary=0
	i=1
	while temp >0:
		remainder=temp%2
		temp=int(temp/2)
		binary+=remainder*i
		i*=10
	print(binary)

def decimal_to_binary2(num):
	tmp=[]
	while num >0:
		tmp.append(num%2 )
		num = int(num/2)
	start=0
	end=len(tmp)-1
	while start < end:
		temp=tmp[start]
		tmp[start]=tmp[end]
		tmp[end]=temp
		start+=1
		end-=1
	print(tmp)

def binary_to_decimal(num):
	temp=int(num)
	remainder=0
	decimal=0
	i=0
	while temp >0:
		remainder=temp%10
		temp=int(temp/10)
		decimal+=remainder*pow(2,i)
		i+=1
	print(decimal)

decimal=55
binary=110111
decimal_to_binary1(decimal)
decimal_to_binary2(decimal)
binary_to_decimal(binary)

