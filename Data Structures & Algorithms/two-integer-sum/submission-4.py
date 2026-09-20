class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for index,element in enumerate(nums):
            remnant = target - element
            if remnant in nums[index+1:]:
                ans.append(index)
                ans.append(nums.index(remnant,index+1))
                return ans