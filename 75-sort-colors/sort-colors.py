class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap (a, b):
            temp = nums[a] 
            nums[a] = nums[b]
            nums[b] = temp

        i, j, k = 0, 0, len(nums) - 1

        while i <= k:
            if (nums[i] == 0):
                swap(i, j)
                j += 1
            
            elif (nums[i] == 2):
                swap(i, k)
                k -= 1
                i -= 1
            
            i += 1