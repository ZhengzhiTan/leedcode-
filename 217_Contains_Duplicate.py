#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Input: nums = [1,2,3,1]
#Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictv={}
        for value in nums:
            if dictv.__contains__(value):
                return True
            else:
                dictv.update({value:1})
                
        return False
            
