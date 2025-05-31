#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right

        self.right.prev = node
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            # remove lru and remove from cache
            lru = self.left.next
            nxt = lru.next

            self.left.next = nxt
            nxt.prev = self.left

            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
