"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/708074870/
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        digits=[]
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a=digits.pop(-1)
                b = digits.pop(-1)

                if token == '+':
                    digits.append(a+b)
                elif token == '-':
                    digits.append(b-a)
                elif token == '*':
                    digits.append(a * b)
                elif token == '/':
                    digits.append(int(b/a))
            else:
                digits.append(int(token))
        return digits[0]