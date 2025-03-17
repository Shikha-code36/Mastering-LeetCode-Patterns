'''
724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.


Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:    
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:    
The sum of the numbers to the left of index 0 (nums[0] = 2) is equal to the sum of numbers to the right of index 0.


Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000

'''
# Brute Force Approach(prefix sum):
# Time: O(n)
# Space: O(n)

class Solution:
    def pivotIndex(self, nums):
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]

        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]

        total_sum=prefix[n-1]

        for i in range(n):
            left_sum=prefix[i-1] if i>0 else 0
            right_sum=total_sum-prefix[i]
            if left_sum==right_sum:
                return i
        return -1
        
# Optimized Approach:
# Time: O(n)
# Space: O(1)

class Solution:
    def pivotIndex(self, nums):
        total_sum=sum(nums)
        left_sum=0

        for i in range(len(nums)):
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1
        
obj = Solution()
print(obj.pivotIndex([1,7,3,6,5,6]))