#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Steps:
        # 1. Create Trie
        # 2. Search

        ROWS = len(board)
        COLS = len(board[0])
        res = set()
        path = set()
        drs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        root = TrieNode()

        # 1. Create Trie
        for w in words:
            root.addWord(w)

        #############################################################
        def backtrack(r, c, node, word) -> None:
            # out of bound, not in children, already in path
            if (not (0 <= r < ROWS) or not (0 <= c < COLS) or
                board[r][c] not in node.children or
                (r, c) in path):
                return

            path.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
            
            # [backtrack(r + drr, c + drc, node, word) for drr, drc in drs] # visit all 4 directions
            for drr, drc in drs:
              backtrack(r + drr, c + drc, node, word)

            path.remove((r, c))

        #############################################################
        # 2. Search words
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
        return res

        
# @lc code=end

