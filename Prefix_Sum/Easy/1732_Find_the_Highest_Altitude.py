'''
1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

'''

# Brute Force Approach:
# Time: O(n)
# Space: O(n)

# class Solution:
#     def largestAltitude(self, gain):
#         n=len(gain)
#         prefix=[0]*(n+1)
#         prefix[0]=0

#         for i in range(n):
#             prefix[i+1]=prefix[i]+gain[i]
#         return max(prefix)

# Optimized Approach:
# Time: O(n)
# Space: O(1)

class Solution:
    def largestAltitude(self, gain):
        max_altitude=0
        current_altitude=0

        for i in gain:
            current_altitude+=i
            max_altitude=max(max_altitude,current_altitude)
        return max_altitude
    
obj = Solution()
print(obj.largestAltitude([-4,-3,-2,-1,4,3,2])) 