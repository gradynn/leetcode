class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # add reverse edges to equations and values
        syms = set()
        for i in range(len(equations)):
            start, end = equations[i]
            value = values[i]
            equations.append([end, start])
            syms.add(start)
            syms.add(end)
            values.append(1 / value)

        out = []
        for idx, query in enumerate(queries):
            if query[0] not in syms or query[1] not in syms:
                out.append(-1)
                continue
            elif query[0] == query[1]:
                out.append(1)
                continue

            visited = [query[0]]
            stack = [(query[0], 1)]
            while stack:
                current = stack.pop()

                if current[0] == query[1]:
                    out.append(current[1])
                    break

                for i, e in enumerate(equations): 
                    if e[0] == current[0] and e[1] not in visited:
                        stack.append((e[1], current[1] * values[i]))
                        visited.append(e[1])
            
            if len(out) != idx + 1:
                out.append(-1)

        return out