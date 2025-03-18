'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''

# Brute Force Approach:
# Time: O(n^2)
# Space: O(1)

class Solution:
    def subarraySum(self, nums, k):
        count=0

        for i in range(len(nums)):
            prefix_sum=0
            for j in range(i,len(nums)):
                prefix_sum+=nums[j]
                if prefix_sum==k:
                    count+=1
        return count

    
# Optimized Approach:
# Time: O(n)
# Space: O(n)

class Solution:
    def subarraySum(self, nums, k):
        count=0
        prefix_sum=0
        prefix_count={0:1}

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum-k in prefix_count:
                count+=prefix_count[prefix_sum-k]
            if prefix_sum not in prefix_count:
                prefix_count[prefix_sum]=1
            else:
                prefix_count[prefix_sum]=prefix_count[prefix_sum]+1
        
        return count

            

obj = Solution()
print(obj.subarraySum([1, 2, 3, 1, 2, 3],3))

        