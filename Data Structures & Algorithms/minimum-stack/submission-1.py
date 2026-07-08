class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Updating min val
        if len(self.minStack) == 0:
            self.minStack.append(val)
            
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

        # Pushing value
        self.stack.append(val)
        

    def pop(self) -> None:
        # Removing from min stack
        if(self.stack[-1] == self.minStack[-1]):
            self.minStack.pop()

        # Popping value
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]