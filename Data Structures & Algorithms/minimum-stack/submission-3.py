class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        d = self.stack.pop()
        if d < 0:
            self.min = self.min - d

    def top(self) -> int:
        t = self.stack[-1]
        return self.min if t < 0 else self.min + t

    def getMin(self) -> int:
        return self.min
