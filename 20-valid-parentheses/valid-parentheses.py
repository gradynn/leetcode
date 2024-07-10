class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        closing = set([')', '}', ']'])

        st = []
        for c in s:
            if c in closing:
                if len(st) == 0 or st.pop() != m[c]:
                    return False
            else:
                st.append(c)
        
        return len(st) == 0