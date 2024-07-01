class Solution:
    def isHappy(self, n: int) -> bool:
        seen = defaultdict(lambda: False)
        while True:
            s1 = 0
            for c in str(n):
                s1 += int(c) ** 2
            n = s1
            
            if n == 1:
                return True
            elif seen[n]:
                return False
            else:
                seen[n] = True
            
            