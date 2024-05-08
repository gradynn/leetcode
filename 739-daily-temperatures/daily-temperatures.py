class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = []
        for idx, temp in enumerate(temperatures[::-1]):
            end = len(stack) - 1
            while stack and stack[end][1] <= temp:
                stack.pop(end)
                end = len(stack) - 1
            if not stack:
                out.append(0)
            else:
                out.append(idx - stack[end][0])
            stack.append((idx, temp))

        return reversed(out)