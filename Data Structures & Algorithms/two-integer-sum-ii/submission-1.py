class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1

