class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:          

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)

            return arr

        def merge(arr, l, m, r):
            leftSide, rightSide = arr[l: m+1], arr[m+1: r+1]
            i, j, k = l, 0, 0

            while j < len(leftSide) and k < len(rightSide):
                if leftSide[j] <= rightSide[k]:
                    arr[i] = leftSide[j]
                    j += 1
                
                else:
                    arr[i] = rightSide[k]
                    k += 1
                
                i += 1
            
            while j < len(leftSide):
                arr[i] = leftSide[j]
                j += 1
                i += 1
            
            while k < len(rightSide):
                arr[i] = rightSide[k]
                k += 1
                i += 1
            
            return arr

        return mergeSort(nums, 0, len(nums) - 1)