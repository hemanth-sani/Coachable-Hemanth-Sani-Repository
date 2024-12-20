from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:

        char_count = defaultdict()
        for letter in s:
            if letter not in char_count:
                char_count[letter] = 1
            else:
                char_count[letter] += 1
        print(char_count) 
 
        max_freq_count = []
        for word, count in char_count.items():
            heapq.heappush(max_freq_count, [-count, word])
        
        prev = None
        string_holder = ''
        while max_freq_count or prev:
            if prev and not max_freq_count:
                return ""
            count, word = heapq.heappop(max_freq_count)
            string_holder += word
            count += 1
            if prev:
                heapq.heappush(max_freq_count,prev)
                prev = None
            if count != 0:
                prev = [count, word]
        
        return string_holder
