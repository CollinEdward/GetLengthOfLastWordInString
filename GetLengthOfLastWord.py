
class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
        lis = list(s.split())
        return len(lis[-1])
