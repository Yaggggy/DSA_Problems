class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s):
            string_index = i + 1
            reversed_alphabet_index = ord('z') - ord(char) + 1
            total += string_index * reversed_alphabet_index
        return total