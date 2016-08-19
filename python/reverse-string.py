#Author: Maple0
#Github:https://github.com/Maple0
#11th Aug 2016


#Giving a string, move the first n numbers of characters(0 to n) to the end of the string. 
#For example, a given string "abcdefg", move the first 2 characters "ab" to the end of the string
#so that the output is "cdefgab"
def reverse_string_left(string,n):
	length=len(string)
	if n <=0 or length ==0 or n>length:
		return string
	left_move_string(string,0,n-1)
	left_move_string(string,n,length-1)
	left_move_string(string,0,length-1)
	return string

#Giving a string, move the last n numbers of the characters(0 to n) to the start of the string. 
#For example, a given string "abcdefg", move the last 2 characters "fg" to the end of the string
#so that the output is "fgabcde"
def reverse_string_right(string,n):
	length=len(string)
	if n <=0 or length ==0 or n>length:
		return string

	left_move_string(string,0,length-1-n)
	left_move_string(string,length-n,length-1)
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

string=["a","b","c","d","e","f","g"]
print(reverse_string_left(string,2))
string=["a","b","c","d","e","f","g"]
print(reverse_string_right(string,2))