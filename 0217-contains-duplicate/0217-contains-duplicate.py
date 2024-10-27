class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()
        
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False

       #METHID 2 
        set1= set(nums)
        lst = list(set1)
        if(len(lst)==len(nums)):
            return False
        else:
            return True