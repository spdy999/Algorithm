# Delete Node in BST

[Account Login - LeetCode](https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1025/)

[https://www.youtube.com/watch?v=wMyWHO9F1OM&ab_channel=TimothyHChang](https://www.youtube.com/watch?v=wMyWHO9F1OM&ab_channel=TimothyHChang)

3 Cases of deleted node

- No child
- one child
    - left or right
- 2 children

```python
# https://www.youtube.com/watch?v=wMyWHO9F1OM&ab_channel=TimothyHChang

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key: # found wanted delete node
            # 4 cases
            if not root.left and not root.right: # 1. no child => simply remove the Node
                return None
            
            if root.left and not root.right: # 2. only "left" child => replace the node with "left" child
                return root.left
            
            if not root.left and root.right: # 3. only "right" child => replace the node with "right" child
                return root.right
            
            if root.left and root.right: # 4. 2 children => replace the node with "in-order successor"
                pnt = root.right
                while pnt.left:
                    pnt = pnt.left
                root.val = pnt.val # swap "deleted node val" with its "inorder succesor val"
                
                root.right = self.deleteNode(root.right, root.val) # find and remove the inorder succesor node (root.val)
            
        
        if root.val < key: # traverse to "right" side
            root.right = self.deleteNode(root.right, key)
        else: # traverse to "left" side
            root.left = self.deleteNode(root.left, key)
        
        return root
```

![Untitled](Delete%20Node%20in%20BST.png)

![Untitled](Delete%20Node%20in%20BST-1.png)

![Untitled](Delete%20Node%20in%20BST-2.png)