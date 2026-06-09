class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if(numbers[i]+numbers[j] == target):
                    n.append(i+1)
                    n.append(j+1)    
                    return n               
