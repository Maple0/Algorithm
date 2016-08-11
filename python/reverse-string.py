#Author: Maple0
#Github:https://github.com/Maple0
#11th Aug 2016
#Giving a string, move n numbers of the characters(0 to n) to the end of the string. 
#For example, a given string "abcdefg", move the first 2 characters "ab" to the end of the string
#so that the output is "cdefgab"
def reverse_string(string,n):
	length=len(string)
	if n <=0 or length ==0 or n>length:
		return string
	left_move_string(string,0,n-1)
	left_move_string(string,n,length-1)
	left_move_string(string,0,length-1)
	return string

def left_move_string(string,start,end):
	while start < end:
		tmp=string[start]
		string[start]=string[end]
		string[end]=tmp
		start=start+1
		end=end-1
	return string

string=["a","b","c","d","e","f"]
print(reverse_string(string,2))