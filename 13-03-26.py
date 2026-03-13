from collections import defaultdict


class Solution(object):
    
    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())

    groupAnagrams(["eat","tea","tan","ate","nat","bat"])