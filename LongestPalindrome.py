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