class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        hash_map = {}
        for right in range(len(s)):
            if s[right] in hash_map:
                hash_map[s[right]]+=1
            else:
                hash_map[s[right]]=1
            while hash_map[s[right]] > 1:
                hash_map[s[left]]-=1
                left+=1
            max_len = max(max_len,right - left + 1)
        return max_len

        