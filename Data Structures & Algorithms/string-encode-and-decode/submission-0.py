class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            result += str(length) + '#' + s
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            num = ""
            while s[i]!='#':
                num+=s[i]
                i+=1
            num = int(num)
            word = ""
            for j in range(i+1,i+1+num):
                word+=s[j]
            result.append(word)
            i = i+1+num
        return result

