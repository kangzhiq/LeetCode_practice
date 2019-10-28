# Longest Palindromic Substring

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Special cases:
Input: ""
Output: ""

Special cases:
Input: "ac"
Output: "a"
'''

# Update 18/10/2019
# new solution with O(n^2) time
# Runtime 56 ms
'''
In fact, this algorithm is working when the poniter passes the middlle point of the exsiting Palindrome. After the middle point, when can either increase the palindrome by one char for the case of "bb" or by two chars for the case of "aba"
'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

# First submission:
# Time and storage complexity is too high 
# 1240 ms with 14 MB memory usage
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_len = 0
        max_start = 0
        for i in range(0, len(s)-1):
            start = i-1
            end = i+1
            while start >= 0 and s[i] == s[start]:
                start -= 1
            while end <= len(s)-1 and  s[i] == s[end]:
                end += 1
            while start>=0 and end<=len(s)-1 and s[start]==s[end]:
                start -= 1
                end += 1
            
            if end-start-1 > max_len:
                max_len = end-start-1
                max_start = start+1
        return s[max_start:max_start+max_len]