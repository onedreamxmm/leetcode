'''
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that 
result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
'''
class Solution(object):
	def sum(self, nums):
		left = [0]*len(nums)
		right = [0]*len(nums)
		res = [0]*len(nums)
		for i in range(1, len(nums)):
			left[i] = left[i - 1] + (nums[i] - nums[i - 1])*i
		for i in range(len(nums) - 2, -1, -1):
			right[i] = right[i + 1] + (nums[i + 1] - nums[i])*(len(nums) - i - 1)
		for i in range(len(nums)):
			res[i] = left[i] + right[i]
		return res
if __name__ == "__main__":
	nums = [2,3,5]
	o = Solution()
	print(o.sum(nums))