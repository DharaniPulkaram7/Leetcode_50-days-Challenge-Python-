class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        List=[]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
            if(dic[nums[i]]==2):
                List.append(nums[i])
        return List