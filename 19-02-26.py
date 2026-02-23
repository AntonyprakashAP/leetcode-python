
"""
 in this case we have an binary string and that will be came with grouped consecutively.
 binary strings only contain 0's and 1's
 so what is consecutive binary string
        - it will looks like this 10101 or 000111 or 00110011
        - what need to find is 
            - what are the binary strings that occurs multple time (how to find it)
                - if the given binary is like this 10101 to find it like this (10 01 10 01 = 4 times) (for 000111 => 000111 0011 01 = 3 times ) (for 00110011 => 0011 01 10 1100 01 10 0011 = 6 times)
"""

class Solution(object):
    def __init__(self, value):
        self.value = value
    def countBinarySubstrings(s):
        """
        :type s: str
        :rtype: int
        """
        pre = 0
        cur = 1
        ans = 0
        print(len(s))
        for i in range(1,len(s)):
            if(s[i-1] == s[i]):
                cur += 1
            else:
                ans += min(pre,cur)
                pre = cur
                cur = 1
        ans += min(pre,cur)
        return ans
    countBinarySubstrings("10101")




""" 
696. Count Binary Substrings

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'. 
>>>>>>> 62668963ba2a0b2b2028bdb17afff1ffef58b7a2
"""