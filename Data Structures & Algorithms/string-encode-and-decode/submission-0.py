class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ""
        for i in strs:
            new_strs = new_strs+str(len(i))+"#"+i
        return new_strs
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j = j + 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res



