class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) >=1 and len(nums) <= 10 ** 4:
            a = 0
            values = []
            zeroes = []
            
            for i in nums:
                if i == 0:
                    a+=1
                else:
                    values.append(i)
            zeroes = [0 for i in range(a)]
            s = sorted(nums)
            if a == 0:
                pass
            else:
                nums[:] = values + zeroes
            
        
        
        