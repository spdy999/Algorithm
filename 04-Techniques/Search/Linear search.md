# Linear search

![[Singly Linked-List.png]]

---

```jsx
const linearSearch = (list, n) => {
    for (let i = 0; i < list.length; i++) {
        if(list[i] === n) return true
    }
    return false
}

module.exports = linearSearch
```

```jsx
const linearSearch = require("./linear-search");

test('Should return true if has in list', () => {
    const list = [0, 1, 2, 3, 4]
    expect(linearSearch(list, 1)).toBe(true)
})

test('Should return false if dont has in list', () => {
    const list = [0, 1, 2, 3, 4]
    expect(linearSearch(list, 10)).toBe(false)
})
```

---

```java
static void linearSearch(int[] lst, int v) {
	int n = lst.length;
	for (int i = 0; i < n; i++) {
		if (lst[i] == v) {
			System.out.println("found! It is at" + i);
			return;
		}
	}
	System.out.println("the element is not in the array");
	return;
}
```