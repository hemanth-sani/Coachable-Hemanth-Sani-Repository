from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_count = 0
        cur_count = 0
        prev_word = deque()
        for i in range(len(s)):
            if s[i] in prev_word:
                if(prev_count < cur_count):
                    prev_count = cur_count
                j = 0
                while s[i] in prev_word:
                    prev_word.popleft()
                    j += 1
                
                prev_word.append(s[i])
                cur_count = len(prev_word)
            else:
                prev_word.append(s[i])
                cur_count += 1
        if prev_count > cur_count:    
            return prev_count
        else:
            return cur_count
