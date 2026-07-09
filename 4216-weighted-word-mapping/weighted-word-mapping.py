class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans  = []
        for word in words:
            sum = 0
            for character in word:
                sum += weights[ord(character) - ord("a")]
            ans.append(chr(ord("z") - sum % 26))
        return "".join(ans) 
        