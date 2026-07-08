import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops ={"+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv
            }

        numbers = []

        for n in tokens:

            # n is a number
            if n not in ops:
                numbers.append(int(n))

            # n is an operator
            else:
                n1 = numbers.pop()
                n2 = numbers.pop()
                numbers.append(int(ops[n](n2, n1)))
        
        return numbers.pop()