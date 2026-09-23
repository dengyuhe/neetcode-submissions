class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={} # char:freq
        left,maxLength=0,0
        for right in range(len(s)):
            windowLength=right-left+1
            count[s[right]]=1+count.get(s[right],0)
            maxFreq=max(count.values())
            if windowLength-maxFreq>k:
                count[s[left]]-=1
                left+=1
            maxLength=max(maxLength, right-left+1)
            right+=1
        return maxLength