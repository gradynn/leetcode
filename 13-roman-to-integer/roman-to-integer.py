class Solution:
    def romanToInt(self, s: str) -> int:
        trans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(0, len(s) - 1):
            if trans[s[i]] < trans[s[i + 1]]:
                total -= trans[s[i]]
            else:
                total += trans[s[i]]
        total += trans[s[-1]]
        
        return total