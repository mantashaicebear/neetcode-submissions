class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = []
        newnums = sorted(nums)
        for i in range(len(newnums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if ((newnums[i]+newnums[left]+newnums[right]) == 0):
                    s1 = []
                    s1.append(newnums[i])
                    s1.append(newnums[left])
                    s1.append(newnums[right])
                    if s1 not in n:
                        n.append(s1)

                    left += 1
                    right -= 1
                
                elif(newnums[i]+newnums[left]+newnums[right] < 0):
                    left +=1
                    
                else:
                    right-=1
        return n
