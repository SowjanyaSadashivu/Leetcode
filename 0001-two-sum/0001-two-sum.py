class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        if not nums:
            return []
        for i in range(len(nums)):
            if nums[i] in index:
                return index[nums[i]], i
            else:
                index[target - nums[i]] = i
        
            
        
        
        
                