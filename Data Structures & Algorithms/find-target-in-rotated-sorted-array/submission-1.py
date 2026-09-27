class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            m = l+(r-l) // 2
            if target==nums[m]:
                return m
            # left portion ordered
            if nums[l]<=nums[m]:
                # if target in ordered left portion
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            #right portion ordered
            else:
                # if target in ordered right portion
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1