---
Updated: 2024-07-14
---
# Depth First Search (DFS)

![[Singly Linked-List.png]]%20153ce2c90d75441ba8d4a2d5be65eea6/Untitled.png)

- don't care about the best path just want to find the destination as fast as possible

- Time complexity $O(V+E)$
    - Nodes + Edges

# [Traversal](https://en.wikipedia.org/wiki/Tree_traversal)
![[04-Techniques/Search/Graph/Depth First Search (DFS)/Untitled.png]]

- **Preorder** (Root, Left, Right)
- **Inorder** (Left, Root, Right)
- **Postorder** (Left, Right, Root)

## Preorder traversal

<aside>
💡 Root, Left, Right

</aside>

<aside>
💡 **first** value is **root**

</aside>

```python
# Hackerrank challenge: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
**def preOrder(root):
    #Write your code here
    if root:
        print(root, end=" ")
        preOrder(root.left)
        preOrder(root.right)**

# Input (stdin)
# 6
# 1 2 5 3 6 4

# Expected Output
# 1 2 5 3 4 6

```

## **Inorder**

<aside>
💡 (Left, Root, Right)

</aside>

<aside>
💡 If BST, inorder traversal is in **ascending** order

</aside>

```python
# Hackerrank challenge: https://www.hackerrank.com/challenges/tree-inorder-traversal/submissions/code/229878373
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

**def inOrder(root):
    # Write your code here
    if root:
        # traverse the left of root
        inOrder(root.left)
        # print the root node
        print(root.info, end=" ")
        # traverse the right of root
        inOrder(root.right)**

# Input (stdin)
# 6
# 1 2 5 3 6 4
# Expected Output
# 1 2 3 4 5 6
```

## **Postorder**

<aside>
💡 (Left, Right, Root)

</aside>

<aside>
💡 **last** value is **root**

</aside>

```python
# Hackerrank challenge: https://www.hackerrank.com/challenges/tree-postorder-traversal/submissions/code/229878807
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

**def postOrder(root):
    # Write your code here
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root, end=" ")**

# Input (stdin)
# 6
# 1 2 5 3 6 4
# 
# Expected Output
# 4 3 6 5 2 1

# Input (stdin)
# 15
# 1 14 3 7 4 5 15 6 13 10 11 2 12 8 9
#
# Expected Output
# 2 6 5 4 9 8 12 11 10 13 7 3 15 14 1
```