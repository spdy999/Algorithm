#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
class TreeNode:
    def __init__(self):
        self.children = dict()  # { 'c': TreeNode() }
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def dfs(self, word, treenode: Optional[TreeNode()]):
        if word is None:
            return treenode.endOfWord

        for i, c in enumerate(word):
            if c in treenode.children:
                treenode = treenode.children[c]
            elif c == '.':
                return any([self.dfs(word[i + 1:], child) for child in treenode.children.values()])
            else:
                return False
        return treenode.endOfWord


    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

