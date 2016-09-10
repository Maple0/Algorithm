#Author: Maple0
#Github:https://github.com/Maple0
#4th Sep 2016
#Given a collection of intervals, merge all overlapping intervals.
#For example,
#Given [1,3],[2,6],[8,10],[15,18],
#return [1,6],[8,10],[15,18].

class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Merge_ResultSet(object):
  def __init__(self,is_modified,merged_numbers):
    self.is_modified = is_modified
    self.merged_numbers = merged_numbers

class Solution(object):
  def inner_merge(self,numbers):
    is_modified=False
    length=len(numbers)
    merged_numbers=[numbers[0]]
    for i in range(1,length):
      c_start=numbers[i].start
      c_end=numbers[i].end
      check_status=0
      for merged_num in merged_numbers:
        m_start=merged_num.start
        m_end=merged_num.end
        if c_start >= m_start and c_end <=m_end:
          check_status=1
        if c_start < m_start and c_end>=m_start and c_end <= m_end:
          merged_num.start=c_start
          check_status=2
        elif c_start >= m_start and c_start<=m_end and c_end > m_end:
          merged_num.end=c_end
          check_status=2
        elif c_start<= m_start and c_end>=m_end:
            if merged_num.start!=c_start:
              merged_num.start=c_start
              check_status=2
            if merged_num.end!=c_end:
              merged_num.end=c_end
              check_status=2
      if check_status==0:
        merged_numbers.append(numbers[i])
      if check_status==2:
        is_modified=True
    return Merge_ResultSet(is_modified,merged_numbers)

  def merge(self, numbers):
    length=len(numbers)
    if length < 2:
      return numbers
    result=self.inner_merge(numbers)
    while result.is_modified==True:
      result=self.inner_merge(numbers)
    return result.merged_numbers

num3=[Interval(1,3),Interval(0,6),Interval(7,7),Interval(8,9),Interval(0,10)]
results=Solution().merge(num3)
for x in results:
  print(x.start,x.end)

 