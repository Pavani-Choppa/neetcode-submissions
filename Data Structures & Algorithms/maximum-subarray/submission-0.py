class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum ,maxSum= 0,float('-inf')
        if not nums:
            return 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum > maxSum:
                maxSum = Sum
            if Sum < 0:
                Sum = 0
        return maxSum