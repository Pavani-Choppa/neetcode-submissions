class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     current = nums[left] + nums[right]
        #     if current == target:
        #         return [left,right]
        #     elif target > current:
        #         left += 1
        #     else:
        #         right -= 1      

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]] = i  