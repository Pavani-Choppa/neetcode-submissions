class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            current = nums[left] + nums[right]
            if current == target:
                return [left+1,right+1]
            elif target > current:
                left += 1
            else:
                right -= 1