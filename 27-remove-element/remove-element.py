class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i, k = 0, 0

        # while i < len(nums):
        #     if nums[i] == val:
        #         k += 1
        #         nums.pop(i)
        #         continue
        #     i += 1
        
        # return len(nums)

        ## two-pointer
        write = 0

        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        
        return write