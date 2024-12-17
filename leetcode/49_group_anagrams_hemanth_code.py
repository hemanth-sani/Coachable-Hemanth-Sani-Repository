class Solution:
    def sort_string(self, word):
        alphabet_count = [0] * 26
        
        sorted_string = ''
        for char in word.replace(" ",""):
            alphabet_count[ord(char)-ord('a')] += 1
        for alphabet_index, count in enumerate(alphabet_count):
            if count > 0:
               sorted_string += chr(alphabet_index + ord('a')) * count
        return sorted_string

    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_strings = {}
        first_string = self.sort_string(strs[0])
        for i in strs[0]:

            first_string = ''.join(first_string)
            group_strings[first_string] = []
        
        for i in range(len(strs)):
            sorted_str = self.sort_string(strs[i])
            sorted_str = ''.join(sorted_str)
            if sorted_str in group_strings:
                group_strings[sorted_str].append(strs[i])
            else:
                group_strings[sorted_str] = []
                group_strings[sorted_str].append(strs[i])
        return list(group_strings.values())
 
