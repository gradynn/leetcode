class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        operators = set(['+', '-', '*', '/'])
        operations = {
            '+': lambda a,b: a + b,
            '-': lambda a,b: a - b,
            '*': lambda a,b: a * b,
            '/': lambda a,b: int(a / b),
        }
        for token in tokens:
            if token in operators:
                r_operand = s.pop()
                l_operand = s.pop()
                result = operations[token](l_operand, r_operand)
                s.append(result)
            else:
                s.append(int(token))
        
        return s[0]