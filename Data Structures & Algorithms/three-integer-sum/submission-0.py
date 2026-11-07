class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)-1
        i = 0
        for i in range(len(nums)):
            if nums[i] != nums[i-1] or i==0:
                j = i + 1
                k = length
                while j < k:
                    if nums[i]+nums[j]+nums[k]==0:
                        result.append([nums[i], nums[j], nums[k]])
                        j+=1
                        while nums[j] == nums[j-1] and j <k:
                            j+=1
                    elif nums[j]+nums[k]<-nums[i]:
                        j+=1
                    else:
                        k-=1
        return result

