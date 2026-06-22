class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        n=len(s)
        Maxlen=0
        d={}
        while(right<n):
            if(s[right] in d and d[s[right]]>=left):
                left=d[s[right]]+1
            Maxlen=max(Maxlen,right-left+1)
            d[s[right]]=right
            right+=1
        return Maxlen
        