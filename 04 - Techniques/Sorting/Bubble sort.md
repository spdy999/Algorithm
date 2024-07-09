# Bubble sort

- Pseodocode

```
		repeat until no swaps
			for i from 0 to n-2
				if i'th and i+1'th elements are out of order
					swap them
```

```java
		
    1 	static void bubbleSort(int[] lst) {
    2 		int n = lst.length;
    3 		boolean swapped;
    4 		do 
    5 		{
    6 			swapped = false;
    7 			for (int i = 0; i < n-1; i++) {
    8 				if (lst[i] > lst[i+1]) {
    9 					int temp = lst[i];
   10 					lst[i] = lst[i+1];
   11 					lst[i+1] = temp;
   12 					swapped = true;
   13 				}
   14 			}
   15 		} while (swapped == true)
   16 		
   17 		System.out.println(Arrays.toString(lst));
   18 	}

https://courses.edx.org/courses/course-v1:Microsoft+DEV285x+1T2018a/courseware/2ce07ccdffe34b77bc2dd79e52807dab/6b702b479cc04f9eabdb704587a67833/1?activate_block_id=block-v1%3AMicrosoft%2BDEV285x%2B1T2018a%2Btype%40vertical%2Bblock%40c6a8661b0e24440aa8a5e8a9e718ad8c
```

```python
	def bubbleSort(lst: List[int]) {
		n = len(lst)
		swapped = True
		while swapped:
			swapped = False
			for i in range(n - 1): #O(n)
				if lst[i] > lst[i+1]:
					lst[i], lst[i+1] = lst[i+1], lst[i]
					swapped = True
	
	}
```