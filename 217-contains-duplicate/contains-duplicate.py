class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        in_set = set()

        for num in nums:
            if num in in_set:
                return True
            
            in_set.add(num)
        
        return False
