# Given an array of integers and a target
class Solution:
    def two_sum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                # if the sum of 2 elements in an array is equal to target
                if (nums[i] + nums[j] == target):
                    # print their index
                    print('Index of elements whos sum is equal target: ', i, j)


s = Solution()
s.two_sum([2, 3, 4], 6)
