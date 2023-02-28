You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


answer1: 
  找规律嘛。。
  斐波那契规律
 class Solution:
    def climbStairs(self, n: int) -> int:
        stair1 = 1
        stair2 = 2
        output = 3
        tmp = 0
        if n == 1:
            output = 1
            return output
        if n == 2:
            output = 2
            return output
        elif n > 2:
            for i in range(0,n-2):
                output = stair1 + stair2
                stair1 = stair2
                stair2 = output
            return output
        else:
            return output
          
answer2:
  斐波那契有个帅气的公式。。
  我感觉这玩意儿迁移性太低了。而且我莫名其妙不成共好气啊
  
