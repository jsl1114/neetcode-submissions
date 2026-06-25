class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operations = "+-*/"
        stack = []

        for curOp in tokens:
            if curOp in operations:
                op1, op2 = int(stack.pop(-2)), int(stack.pop(-1))
                if curOp == '+':
                    stack.append(op1 + op2)
                elif curOp == '-':
                    stack.append(op1 - op2)
                elif curOp == '*':
                    stack.append(op1 * op2)
                elif curOp == '/':
                    stack.append(op1 / op2)
            else:
                stack.append(curOp)
            print(stack)
        
        return stack[0]