# Increasing Triplet Subsequence

'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Examples:

Input: [1,2,3,4,5]
Output: true

Input: [5,4,3,2,1]
Output: false

Special cases:

Input: [1,1,1,1,1]
Output: false
'''

# Update 28/10/2019
# Complexity of max() is an additional O(n), replace it by Inf would be a good choice
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

# O(n) time complexity
# Runtime 60ms
# beats 91.5%

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False
        
        first = second = max(nums)+1
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False