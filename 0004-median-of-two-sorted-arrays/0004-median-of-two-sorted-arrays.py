class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lists = nums1 + nums2
        lists.sort()
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[n-1]        
        elif n >= 2:
            if n % 2 != 0:
                return lists[n//2]
            else:
                m = n // 2
                return ((lists[m-1] + lists[m])/2)
            
             
        