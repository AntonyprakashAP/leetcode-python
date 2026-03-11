class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = sorted(s)
        st = sorted(t)

        return True if ss == st else False

    print(isAnagram("nagaram","anagrm"))