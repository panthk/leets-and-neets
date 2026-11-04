class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} #key is the number, value is it's frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1
          
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)

        mostK = []
        for i in freq[::-1]:
            for num in i:
              mostK.append(num)
              if (len(mostK) == k):
                print(len(mostK))
                return mostK

        