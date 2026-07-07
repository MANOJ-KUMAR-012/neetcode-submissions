class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1 = "".join(sorted(s1))

        for i in range(len(s2) - len(s1) + 1):

            word = s2[i:i+len(s1)]

            word = "".join(sorted(word))

            if word == s1:
                return True

        return False