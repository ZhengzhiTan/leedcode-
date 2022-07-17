##method 1 two loop
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1,num in enumerate(nums):
            for index2 in range(index1+1,len(nums)):
                if num + nums[index2] == target:
                    return [index1,index2]
## method 2 two pivots
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        nums_sorted = sorted(nums)
        print(nums)
        while left < right:

            if nums_sorted[left] + nums_sorted[right] == target:
                print(nums)
                nums_leftindex = nums.index(nums_sorted[left])
                nums_rightindex =nums.index(nums_sorted[right])
                if nums_leftindex == nums_rightindex:
                    nums_rightindex =nums.index(nums_sorted[right],nums.index(nums_sorted[left])+1)
                    return [nums_leftindex,nums_rightindex]
                else:
                    return [nums_leftindex,nums_rightindex]

                
            elif nums_sorted[left] + nums_sorted[right] > target:
                right = right - 1
            else:
                left = left + 1

        return [-1]
## hash map/ dict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictc = {}
        for index,num in enumerate(nums):

            if target-num in dictc:
                return [dictc.get(target-num),index]
            else:
                dictc.update({num:index})
