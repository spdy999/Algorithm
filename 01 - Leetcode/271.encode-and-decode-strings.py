#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode And Decode Strings
#

# @lc code=start
class Codec:
    delimiter = '#,|&'
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        strr = self.delimiter.join(strs)
        return strr
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.delimiter)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
        
# @lc code=end

