class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)] # the freq <= len(nums)
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items(): # go throught the key-value pair in dict
            freq[c].append(n) # add count to freq

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res



    # my thought
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count={}
    #     for i in range(len(nums)):
    #         count[nums[i]]=1+count.get(nums[i],0)
    #     sortedcount = sorted(count, key=count.get, reverse=True)
    #     return sortedcount[:k]