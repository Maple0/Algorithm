
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

print(insert_sort([2,8,7,1,6,9,13]))

   
 
 