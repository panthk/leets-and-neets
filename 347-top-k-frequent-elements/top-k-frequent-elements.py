class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} #key is the number, value is it's frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1
          
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)

        # mostK = []
        # for i in freq[::-1]:
        #     for num in i:
        #       mostK.append(num)
        #       if (len(mostK) == k):
        #         print(len(mostK))
        #         return mostK

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res