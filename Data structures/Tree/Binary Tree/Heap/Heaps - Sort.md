# Heaps - Sort

<aside>
💡 Building a heap just to sort it might not be a good way to go 😅

</aside>

```java
public void sort() {
        int lastHeapIndex = size - 1;
        for (int i = 0; i < lastHeapIndex; i++) {
            // swap first and last heap
            int tmp = heap[0];
            heap[0] = heap[lastHeapIndex - i];
            heap[lastHeapIndex - i] = tmp;

            fixHeapBelow(0, lastHeapIndex - i - 1);
        }
    }
```

```java
heap.printHeap(); // 80, 75, 60, 68, 55, 40, 52, 67,
heap.sort();
heap.printHeap(); // 40, 52, 55, 60, 67, 68, 75, 80,
```