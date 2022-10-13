class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dict = {}
        start = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in dict and start <= dict[s[i]]:
                start = dict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            dict[s[i]] = i
        return max_length
                
        