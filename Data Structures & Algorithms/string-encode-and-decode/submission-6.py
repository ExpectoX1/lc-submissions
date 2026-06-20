class Solution:

    def encode(self, strs: List[str]) -> str:
        e_strs = ""
        for st in strs:
            l = len(st)
            e_strs += f'{l}#{st}'
        return e_strs

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':        
                j += 1
            length = int(s[i:j])     
            word = s[j + 1 : j + 1 + length]  
            res.append(word)
            i = j + 1 + length 
        return res