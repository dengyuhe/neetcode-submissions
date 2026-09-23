class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # char -> most recent index
        left = 0
        maxLength = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            maxLength = max(maxLength, right - left + 1)
        return maxLength