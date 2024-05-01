class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        if a | b == c:
            return count

        aBin, bBin, cBin = bin(a)[2:], bin(b)[2:], bin(c)[2:]

        maxLen = max(len(aBin), len(bBin), len(cBin))
        for i in range(maxLen - len(aBin)):
            aBin = "0" + aBin
        for i in range(maxLen - len(bBin)):
            bBin = "0" + bBin
        for i in range(maxLen - len(cBin)):
            cBin = "0" + cBin

        for i in range(len(cBin)):
            if int(cBin[i]):
                if not int(aBin[i]) and not int(bBin[i]):
                    count += 1
            else:
                if int(aBin[i]) and int(bBin[i]):
                    count += 2
                elif int(aBin[i]) != int(bBin[i]):
                    count += 1

        return(count)