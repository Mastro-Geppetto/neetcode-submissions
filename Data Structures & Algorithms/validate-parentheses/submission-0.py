class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        s = s[::-1]
        print(s)
        for c in s:
            print(c, " ", end="")
            if c == '}' or c == ']' or c == ')':
                print('insert')
                stack.append(c)
            else:
                print('pop', end="")
                if len(stack) == 0:
                    print('empy st')
                    return False
                _ = stack.pop(-1)
                print(" ", _, end=" ")
                if c == '{' and _ == '}':
                    continue
                elif c == '[' and _ == ']':
                    continue
                elif c == '(' and _ == ')':
                    continue
                else:
                    print(" failed ",stack)
                    return False
        if len(stack) > 0:
            print('not empty')
            return False
        return True