Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

  
  answer1:
    class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tmp = nums[0]
        length = len(nums)
        for i in range(1,length):
            print(i)
            nums[i] = nums[i] + tmp
            tmp = nums[i]
        return nums
      
  running time O(N)
  space O (N)
