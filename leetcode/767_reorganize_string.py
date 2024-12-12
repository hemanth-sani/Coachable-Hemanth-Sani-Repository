from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCount = Counter(s)
        maxFreqCount = []
        for word, count in charCount.items():
            heapq.heappush(maxFreqCount, [-count, word])
        
        prev = None
        stringHolder = ''
        while maxFreqCount or prev:
            if prev and not maxFreqCount:
                return ""
            count, word = heapq.heappop(maxFreqCount)
            stringHolder += word
            count += 1
            if prev:
                heapq.heappush(maxFreqCount,prev)
                prev = None
            if count != 0:
                prev = [count, word]
        
        return stringHolder
        
