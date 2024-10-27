class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the slow pointer
        i = 0
        
        # Iterate through the array with the fast pointer
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # Return the number of unique elements
        return i + 1