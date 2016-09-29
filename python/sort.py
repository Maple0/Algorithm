import random
#Author: Maple0
#Github:https://github.com/Maple0
#10th Aug 2016
#Sort by ascending

def insert_sort(list):
    for j in range(1,len(list)):
        key=list[j]
        i=j-1
        while i>=0 and list[i]>key:
            list[i+1]=list[i]
            i=i-1
        list[i+1]=key
    return list

def quick_sort(list,left,right):
	if len(list)<2:
		return list
	if left < right:
		i=left
		j=right
		x=list[left]
		while  i < j:
			while i< j and list[j]>=x:
				j-=1
			if i<j:
				list[i]=list[j]
				i+=1
			while i< j and list[i]<=x:
				i+=1
			if i<j:
				list[j]=list[i]
				j-=1
		list[i]=x
		quick_sort(list,left,i-1)
		quick_sort(list,i+1,right)
	return list

nums=[]
for x in range(0,1000000):
	nums.append(random.randint(1, 10000))

#insert_sort(nums)
quick_sort(nums,0,len(nums)-1)
   
 
 