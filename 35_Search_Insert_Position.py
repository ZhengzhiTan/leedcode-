#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

#Input: n = 5, bad = 4
#Output: 4
#Explanation:
#call isBadVersion(3) -> false
#call isBadVersion(5) -> true
#call isBadVersion(4) -> true
#Then 4 is the first bad version.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        Start = 0
        End = len(nums)-1
        if End == Start:
            if nums[Start] >= target:
                return Start
            else:
                return Start +1
        if nums[End] < target:
            return End +1
        if nums[Start] > target:
            return Start
        while Start < End:

            locate = (Start+End)//2
            if nums[locate] == target:
                return locate
            elif nums[locate] > target:
                End = locate 
            else:
                Start = locate

            if End - Start == 1:
                if nums[Start] == target:
                    return Start
                elif nums[End] == target:
                    return End
                else:
                    return End
