class Solution:
    def firstUniqChar(self, s: str) -> int:
        x = Counter(s)
        a = []
        for i in x.items():
            if i[1] == 1:
                a.append(i[0])
            pass
        if len(a) == 0:
            return -1
        else:
            return s.index(a[0])
        
        