class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        out = []
        if len(digits) == 0:
            return []
 
        def dfs(digits, string):
            if len(digits) == 0:
                out.append(string)
                return
            for c in mapping[digits[0]]:
                dfs(digits[1:], string + c)
        dfs(digits, "")

        return out
