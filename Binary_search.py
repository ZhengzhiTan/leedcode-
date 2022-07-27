#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4

## 分而治之
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Start = 0 
        End = len(nums) - 1 
           
        while (Start != End):
            index = (Start+End)//2
            ##handle special situation 
            if nums[End] < target or nums[Start] > target:
                return -1 
            if target == nums[index]:
                return index
            elif nums[index] > target:
                End = index - 1
            else:
                Start = index + 1
            ## handle no target situation
        if nums[Start] == nums[End]:
            if nums[Start] == target:
                return Start
            else:
                return -1
              

                
