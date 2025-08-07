class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            output = word.index(ch)
            substring = word[:output+1]
            reverse_sub = substring[::-1]
            return reverse_sub + word[output+1:]
        else:
            return word