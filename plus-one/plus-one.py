class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(str(i) for i in digits) 
        n = int(s) + 1
        y = []
        for i in str(n):
            y.append(int(i))
        return y