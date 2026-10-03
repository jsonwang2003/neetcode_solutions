class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_vals) == 0:
            self.min_vals.append(val)
        else:
            self.min_vals.append(min(val, self.min_vals[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]
