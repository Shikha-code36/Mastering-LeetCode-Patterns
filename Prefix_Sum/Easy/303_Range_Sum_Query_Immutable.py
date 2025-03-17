'''
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ..., nums[j]))

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
At most 104 calls will be made to sumRange. 
'''

# Brute Force Approach:
# Time: O(n) for each query
# Space: O(1)

class NumArray:
    def __init__(self, nums):
        self.nums = nums  # Store the array

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1])  # Compute sum from left to right (inclusive)

# Optimized Approach:
# Time: O(1) for each query
# Space: O(n)
# Prefix Sum Technique

'''
arr = [-2, 0, 3, -5, 2, -1]

prefix[0] = arr[0]=-2 n= 6

for i (1,n):
    prefix[1] = prefix[i-1]+arr[i] = -2+0 = -2
    prefix[2] = prefix[1]+arr[2] = -2+3= 1
    prefix[3] = prefix[2]+arr[3] = 1+(-5) = -4
    prefix[4] = -4+2 =-2
    prefix[5] = -2+(-1) = -3


prefix = [-2,-2,1,-4,-2,-3]

sumRange(0,2) 

if l ==0
prefix[r] = prefix[2] = 1

sumRange(2,5)

l=2, r=5

prefix[5]-prefix[2-1] = -3 - (-2) = -1

'''
class NumArray:

    def __init__(self, nums):
        n = len(nums)
        self.prefix = [0]*n
        self.prefix[0] = nums[0]

        for i in range(1,n):
            self.prefix[i]=self.prefix[i-1]+nums[i]

    def sumRange(self, left, right):
        if left==0:
            return self.prefix[right]
        return self.prefix[right]-self.prefix[left-1]
    
# Define the input list
nums = [-2, 0, 3, -5, 2, -1]

# Create an instance of NumArray
numArray = NumArray(nums)

# Test cases
print(numArray.sumRange(0, 2))  # Expected output: 1  => (-2 + 0 + 3)
print(numArray.sumRange(2, 5))  # Expected output: -1 => (3 + (-5) + 2 + (-1))
print(numArray.sumRange(0, 5))  # Expected output: -3 => (-2 + 0 + 3 + (-5) + 2 + (-1))
        

