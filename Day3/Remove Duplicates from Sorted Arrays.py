class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y=1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[y]=nums[i+1]
                y+=1
        return(y)