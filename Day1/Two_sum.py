class Solution:
    def twoSum(self, nums, target):
        hist = {}
        for i, n in enumerate(nums):
            if target - n in hist:
                return [hist[target-n], i]
            hist[n] = i