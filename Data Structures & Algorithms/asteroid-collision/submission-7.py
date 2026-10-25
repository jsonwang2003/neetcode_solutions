class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            ast = asteroids[i]
            if len(stack) == 0:
                stack.append(ast)
                continue

            if ast < 0 and stack[-1] > 0:
                while ast < 0 and stack[-1] > 0:
                    if abs(stack[-1]) == abs(ast):
                        stack.pop()
                        break
                    elif abs(stack[-1]) < abs(ast):
                        stack.pop()
                    elif abs(stack[-1]) > abs(ast):
                        break
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(ast)
                        break
            else:
                stack.append(ast)
                           
        
        return stack