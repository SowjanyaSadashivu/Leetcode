class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        temp = []
        for i in a:
            temp.append(i)
        temp.reverse()
        value = int("".join(temp))
        if x < 0:
            if value >= -(2**31) and value <= (2**31 - 1):
                return -value
            else:
                return 0
        else:
            if value >= -(2**31) and value <= (2**31 - 1):
                return value
            else:
                return 0
        
