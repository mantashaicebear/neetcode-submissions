class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in new_list:
                new_list[key] = []
            
            new_list[key].append(word)

        return list(new_list.values())
        



        