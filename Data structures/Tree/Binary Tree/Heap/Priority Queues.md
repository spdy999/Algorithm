# Priority Queues

> [[Max heap]]
> 

<aside>
💡 Think of Emergency room 🚨 : hear attack 💔 > sneeze 🤧

</aside>

# In java lowest value = highest priority

```java
package com.avenger666.Heap.PriorityQueue;

import java.util.PriorityQueue;

public class PriorityQueueMain {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

        pq.add(25);
        pq.add(-22);
        pq.add(1343);
        pq.add(54);
        pq.add(0);
        pq.add(-3492);
        pq.add(429);

        // -3492, -22, 0, 25, 54, 429, 1343
        // lowest = highest priority
        System.out.println(pq.peek()); // -3492         : -3492, -22, 0, 25, 54, 429, 1343
        System.out.println(pq.remove()); // -3492       : -22, 0, 25, 54, 429, 1343
        System.out.println(pq.peek()); // -22           : -22, 0, 25, 54, 429, 1343
        System.out.println(pq.poll()); // -22  // poll = remove <== remove highest priority : 0, 25, 54, 429, 1343
        System.out.println(pq.peek()); // 0             : 0, 25, 54, 429, 1343
        System.out.println(pq.remove(54));        // : 0, 25, 429, 1343

        System.out.println("------------");
        Object[] ints = pq.toArray();
        for (Object num: ints) {
            System.out.println(num); // 0, 25, 429, 1343
        }
        System.out.println("------------");

        System.out.println(pq.peek()); // 0             : 0, 25, 429, 1343
        pq.add(-1);                                  // : -1, 0, 25, 429, 1343
        System.out.println(pq.peek()); // -1            : -1, 0, 25, 429, 1343
    }
}
```