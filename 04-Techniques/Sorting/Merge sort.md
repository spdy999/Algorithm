# Merge sort

# Top-Down

```python
import math
class Solution:
    def merge(self, sortedLeftArr: List[int], sortedRightArr: List[int]) -> List[int]:
        acc = []
        while len(sortedLeftArr) != 0 and len(sortedRightArr) != 0:
            if sortedLeftArr[0] < sortedRightArr[0]:
                acc.append(sortedLeftArr.pop(0))

            else:
                acc.append(sortedRightArr.pop(0))

        return acc + sortedLeftArr + sortedRightArr
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        length = len(nums)
        pivot = math.floor(length / 2)
        
        sortedLeftArr = self.sortArray(nums[0 : pivot])
        sortedRightArr = self.sortArray(nums[pivot:])
        
        mergeSorted = self.merge(sortedLeftArr, sortedRightArr)
        
        return mergeSorted
        
# sortedLeftArr
# sortedRightArr
# mergeSortedLeftRight
```

```python
def merge(l, r):
	# TODO: sortedLst
	sortedLst = []
	while len(l) and len(r):
		if l[0] < r[0]:
			sortedLst.append(l.pop(0))
		else:
			sortedLst.append(r.pop(0))

	return sortedLst + l + r

def mergeSort(lst):
	n = len(lst)
	if n == 1:
		return lst
	pivot = n // 2
	left = lst[0:pivot]
	right = lst[pivot:]
	return	merge(mergeSort(left), mergeSort(right))

print(mergeSort([3,2,1,4]))	# 1,2,3,4
print(mergeSort([1,2,3,4])) # 1,2,3,4
print(mergeSort([4,3,2,1]))	# 1,2,3,4
print(mergeSort([3,2,5,1,4])) # 1,2,3,4,5
```