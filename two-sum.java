





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
// time complexity O(n)
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

//学习笔记：包装类型1
//基本类型                               //包装类型
// int                                  //integer
//long                                  //Long
//boolean                               //Boolean
//byte                                  //Byte
//char                                  //Character
//flow                                  //FLow
//double                                //Double
//short                                 //Short
// 包装类型 个人理解是java 内嵌的对象。
//为啥要内嵌对象。。他们大部分的处理操作都需要用到对象. 就像arraylist 一样。他需要的对象而不是基本类型。就很操蛋。Python真是误人子弟。用多了python 很难适应。

//学习笔记：包装类型2
//按理说要是包装类型他们都是对象的话。加入value 就好了 直接Integer.valueof(值) 要拆出来就 intValue.
//java 还加了一个 自动填装和自动拆解 就可以直接 integer i = value；

//学习笔记：包装类型3
//对象是可以提供空值NULL的
//但是NUll 在基本类中是不存在 所以给Integer 赋值空集是可以的但是不能用intValue

///学习笔记：包装类型4 
//还有一个就是 包装类之间的自动比较 自动填装 -128-127 是可以自动填装的 但是超过这个就需要调用。 
//学习笔记：对hashmap 的理解。他就是建了个对象嘛。方便好理解哈哈哈。









