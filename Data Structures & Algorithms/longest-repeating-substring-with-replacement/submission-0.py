from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]

            hash_map[char] = hash_map.get(char, 0) + 1

            max_freq = max(max_freq, hash_map[char])

            while (right - left + 1) - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len