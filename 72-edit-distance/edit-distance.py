class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        eD = [[0 for i in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        
        # base case
        for i in range(len(word1) + 1):
            eD[0][i] = i
        for i in range(1, len(word2) + 1):
            eD[i][0] = i

        # bottom-up
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    eD[i][j] = eD[i - 1][j - 1]
                else:
                    eD[i][j] = min(
                        eD[i - 1][j],
                        eD[i][j - 1],
                        eD[i - 1][j - 1]
                    ) + 1

        return eD[len(word2)][len(word1)]