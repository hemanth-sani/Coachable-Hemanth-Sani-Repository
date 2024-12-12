class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_strings = {}
        first_string = sorted(strs[0])
        first_string = ''.join(first_string)
        group_strings[first_string] = []
        
        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            sorted_str = ''.join(sorted_str)
            if sorted_str in group_strings:
                group_strings[sorted_str].append(strs[i])
            else:
                group_strings[sorted_str] = []
                group_strings[sorted_str].append(strs[i])
        return list(group_strings.values())
