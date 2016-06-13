class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        res = []
        dic={}
        exist={}
        
        for i in xrange(n):
            if nums[i] not in dic:
                dic[nums[i]] = i
        for i in xrange(n):
            for j in xrange(i+1,n):
                if -(nums[i] + nums[j]) in dic and dic[-(nums[i] + nums[j])] != i and dic[-(nums[i] + nums[j])] != j:
                    temp = sorted( [nums[i], nums[j], nums[dic[-(nums[i]+nums[j])]]] )
                    if tuple(temp) not in exist:
                        res += [temp]
                        exist[tuple(temp)] = 1
        return res
