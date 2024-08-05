class Solution(object):
    def remove_element(self, nums, val):
        for number in nums:
            if number == val:
                nums.remove(val)

solution = Solution()

nums = [2,3,2,3,2,3]
val = 3

solution.remove_element(nums, val)
print(nums)