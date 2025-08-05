class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        count = 0
        for word in words:
            if word[::-1] in seen:
                count+=1
            else:
                seen.add(word)
        return count
        