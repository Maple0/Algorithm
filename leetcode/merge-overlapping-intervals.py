# Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
                self.start = s
                self.end = e
 
class Solution(object):

  def sort(self,numbers):
    length=len(numbers)
    #tmp=None
    for i in range(0,length-1):
      for j in range(0,length-1-i):
        if numbers[j].start>numbers[j+1].start:
          tmp=numbers[j+1]
          numbers[j+1]=numbers[j]
          numbers[j]=tmp
    return numbers
  def merge(self, numbers):
    if len(numbers) < 2:
      return numbers
    numbers=self.sort(numbers)
    curr_interval=numbers[0]
    last_interval=None
    merged_numbers=[]
    length=len(numbers)
    isOverlapped=False
    if length>1:
      i=1
      while i < length:
        last_interval=numbers[i]
        if last_interval.start<= curr_interval.end and last_interval.end>=curr_interval.end:
          curr_interval.end=last_interval.end
          isOverlapped=True
        else:
          if isOverlapped:
            merged_numbers.append(curr_interval)
            isOverlapped=False
          else:
            merged_numbers.append(curr_interval)
          curr_interval=last_interval
        i+=1
      if isOverlapped:
        merged_numbers.append(curr_interval)
      else:
        merged_numbers.append(last_interval)
    return merged_numbers



numbers=[Interval(1,4),Interval(2,3)]#,Interval(11,13),Interval(2,6),Interval(12,19),Interval(15,18)]
a=Solution().sort(numbers)
for x in a:
  print(x.start,x.end)

result=Solution().merge(numbers)
for x in result:
  print(x.start,x.end)

print('1111111')

numbers=[Interval(1,4),Interval(8,9),Interval(11,13),Interval(2,6),Interval(12,19),Interval(15,18)]
a=Solution().sort(numbers)
for x in a:
  print(x.start,x.end)

result=Solution().merge(numbers)
for x in result:
  print(x.start,x.end)
 