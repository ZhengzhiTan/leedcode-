#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Explanation: After squaring, the array becomes [16,1,0,9,100].
#After sorting, it becomes [0,1,9,16,100]
## 但是Leetcode 的测试数据太小了 nlogn 反而比 n 快
## 先乘在排序
## nlogn
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums2 = []
        #print(len(nums2))
        if length <1:
            return -1
        for tmp in nums:
            locate = tmp * tmp
            #print("locate",locate)
            nums2.append(locate)
        nums2.sort()
        return nums2
      
## 双指针
## n
 class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        out = []
        while (left <= right):

            if abs(nums[left]) < abs(nums[right]):
                out.insert(0,nums[right]*nums[right])
                right = right -1
            else:
                out.insert(0,nums[left]*nums[left])
                left = left + 1
        return out  
      
      class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        out = []
        while (left <= right):
            tmp_left = nums[left]
            tmp_left = nums[left]*tmp_left
            tmp_right = nums[right]
            tmp_right = tmp_right*tmp_right
            if tmp_left < tmp_right:
                out.insert(0,tmp_right)
                right = right -1
            else:
                out.insert(0,tmp_left)
                left = left + 1
        return out
      
      
      class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        out = []
        while (left <= right):

            tmp_left = nums[left] **2

            tmp_right = nums[right] **2
            if tmp_left < tmp_right:
                out.insert(0,tmp_right)
                right = right -1
            else:
                out.insert(0,tmp_left)
                left = left + 1
        return out
