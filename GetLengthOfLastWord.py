class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
            # When we don't tell it where to split it will just split everywhere that isn't a string    
        lis = list(s.split())
        return len(lis[-1])
    
    s = "  - fly me ..  to ,  the moon    "
    print(lengthOfLastWord(s))

    # You can do this is you aren't using return I think another example is

class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        
        lis = list(s.split())
        return len(lis[-1])

    # This will do the same, but you aren't printing, so this is faster and shorter

