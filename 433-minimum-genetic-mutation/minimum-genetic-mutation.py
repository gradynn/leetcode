class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def editDistance(gene1, gene2):
            out = 0
            for i in range(8):
                if gene1[i] != gene2[i]: out += 1
            return out

        q = deque()
        q.append([startGene, 0])
        visited = set()
        while q:
            cur, depth = q.popleft()

            for mutation in bank:
                if mutation not in visited and editDistance(cur, mutation) == 1:
                    visited.add(mutation)
                    if mutation == endGene:
                        return depth + 1
                    q.append([mutation, depth + 1])

        return -1