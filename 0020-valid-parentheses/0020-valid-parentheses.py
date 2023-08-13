class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = {"(", "[", "{"}
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]: # accessing dictionary value
                #stack을 check하는 이유는 stack이 비어있는데 닫는 paranthesis가 오면 안된다         
                stack.pop()
            else:
                return False
        return stack == []