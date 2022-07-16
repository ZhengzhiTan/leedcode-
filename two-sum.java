





/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
*/

// method1 brute force
//time complexity: O(n2)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] error = {};
        for (int pivot1 = 0; pivot1 < nums.length; pivot1 = pivot1 + 1){
            for (int pivot2 = pivot1+1; pivot2 < nums.length; pivot2 = pivot2 + 1){
                if (nums[pivot1] + nums[pivot2] == target){
                    int[] result = {pivot1,pivot2};
                    return result;
                }
            }
        }
        return error;
    }
}


//method2 two pivot
// time complexity O(nlogn)
// if array is sorted, O(n)
import java.util.ArrayList;
public int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int x: nums){
            numbers.add(x);
        }

        ArrayList<Integer> tmp = (ArrayList<Integer>)numbers.clone();
        tmp.sort(Comparator.naturalOrder());

        
        int Left = 0;
        int Right = tmp.size()-1;
        

        while(Left < Right){
            if (tmp.get(Left) + tmp.get(Right) == target){
                int index_Left = numbers.indexOf(tmp.get(Left));
                int index_Right = numbers.indexOf(tmp.get(Right));
                if (index_Left == index_Right){
                    numbers.set(index_Left,tmp.get(Left)+1);
                    index_Right = numbers.indexOf(tmp.get(Right));
                    return new int[]{index_Left,index_Right};
                }else{
                    return new int[]{index_Left,index_Right};
                }
                    
            }else if (tmp.get(Left) + tmp.get(Right) > target){
                Right --;
            }else {
                Left ++;
            }
        }

        return new int[]{};
        }  

// method 3 hash map

public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length;i=i+1){
            int rest = target - nums[i];
            if (map.containsKey(rest)){
                return new int[]{map.get(rest),i};
            }else{
                map.put(nums[i],i);
            }
        }

       
        return new int[]{};
        }  
