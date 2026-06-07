class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 0
            res[i] = res[i] + 1

        new_res = sorted(res.items(), key=lambda x: x[1], reverse = True)
        new_res2 = []
        for i in range(k):
            new_res2.append(new_res[i][0])

        return new_res2