class Solution(object):
    def containsDuplicate(nums):
        setNums = set(nums)
        return False if len(nums) == len(setNums) else True


    print(containsDuplicate([1,2,3,1]))