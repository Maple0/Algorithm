#Author: Maple0
#Github:https://github.com/Maple0
#8st Sep 2016
#Given a sum  and a array, find out the number pairs that has the same sum value
#For example, array= [-2,0,1,2,4,6,7,8,10] sum=8 
#expected output [-2,10],[0,8],[1,7]

def sum_search(arr,sum):
	num_pairs={}
	length=len(arr)
	if len(arr)>1:
		for i in range(0,length/2):
			rem=sum-arr[i]
			for j in range(i+1,length):
				if arr[j]==rem and num_pairs.has_key(rem)==False:
					num_pairs[rem]=[arr[i],arr[j]]
	return num_pairs


array= [-2,0,1,2,4,6,7,8,10]
print(sum_search(array,8))
