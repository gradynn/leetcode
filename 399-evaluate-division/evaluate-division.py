class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        for i in range(len(equations)):
            equations.append([equations[i][1], equations[i][0]])
            values.append(1 / values[i])

        out = []
        for q in queries:
            valid = False
            s, v = [(q[0], 1)], set([q[0]])
            while s:
                cont = False
                cur, quotient = s.pop()
                for i in range(len(equations)):
                    if equations[i][0] == cur:
                        newQ = quotient * values[i]
                        if equations[i][1] == q[1]:
                            out.append(newQ)
                            print(f"Writing {newQ} in query {q[0]}/{q[1]}")
                            valid, cont = True, True
                            break
                        if equations[i][1] not in v:
                            s.append((equations[i][1], newQ))
                            v.add(equations[i][1])
                if cont:
                    break

            if not valid:
                out.append(-1)

        return out