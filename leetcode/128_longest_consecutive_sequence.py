class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = set(nums)
        sort = sorted(ns)
        count = 1
        list1 = []
        
        for i in range(len(sort)-1):
            if(sort[i]<sort[i+1] and (sort[i+1]-sort[i])==1):
                print(sort[i])
                count+=1
            else:
                count=1
            list1.append(count)
            #print(list1)
        if(len(sort)==0):
            return 0
        elif(len(sort)==1):
            return 1
        return max(list1)
        
