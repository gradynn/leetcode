class Solution:
    def intToRoman(self, num: int) -> str:
        hm = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        result = ""
        remaining = num
        while remaining > 0:
            for d in hm:
                if remaining - d >= 0:
                    remaining -= d
                    result += hm[d]
                    break

        return result