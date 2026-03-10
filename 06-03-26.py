class Solution(object):
    def checkOnesSegment(s):
        """
        :type s: str
        :rtype: bool
        """
        idx = 0

        for i in range(len(s)):
            if s[i] == '1':
                if i - idx > 1:
                    return False
                idx = i

        return True
    print(checkOnesSegment("1111"))