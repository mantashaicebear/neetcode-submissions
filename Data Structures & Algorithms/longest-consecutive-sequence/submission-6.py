class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = sorted(nums)
        count = 1
        maxi = 1
        if not nums:
            return 0
        for i in range(len(snums)-1):
            if (snums[i]+1 == snums[i+1]):
                count += 1
            elif (snums[i] == snums[i+1]):
                continue
            else:
                count = 1
            if(count > maxi):
                    maxi = count
        return maxi
        