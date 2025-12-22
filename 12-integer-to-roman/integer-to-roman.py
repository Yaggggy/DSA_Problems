class Solution:
    def intToRoman(self, num: int) -> str:

        value_to_symbols: dict[int, str] = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        value_keys_reversed: list[int] = list(reversed(value_to_symbols.keys()))

        remaining_value: int = num
        final_numerals: list[int] = []

        for value in value_keys_reversed:
            while remaining_value >= value:
                numeral: str = value_to_symbols[value]
                final_numerals.append(numeral)
                remaining_value -= value

        return "".join(final_numerals)