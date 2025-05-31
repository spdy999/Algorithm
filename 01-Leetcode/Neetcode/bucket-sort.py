from collections import Counter

# Check leetcode version. This version can be used only consecutive order
arr = [2, 1, 2, 0, 0, 2]
# arr = [2,0]
counter = Counter(arr)
print(arr)
print(counter)

i = 0
for n in range(len(counter)):
    for _ in range(counter[n]):
        arr[i] = n
        print("i:", i, "n:", n, arr)
        i += 1
print(arr)
