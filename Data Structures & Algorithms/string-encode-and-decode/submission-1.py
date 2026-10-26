class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = "#"
        final = ""
        for string in strs:
            l = str(len(string))
            final += l
            final += sep
            final += string
        return final
            
    def decode(self, s: str) -> List[str]:
        sep = "#"
        final = []
        wl = len(s)
        i = 0
        l = 0
        while i < wl:
            j = s.find(sep, i)
            l = int(s[i:j])
            final.append(s[j+1:j+1+l])
            i = j + 1 + l
        return final
