class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if s.is_empty:
            return "The stack is empty."

        return s.stack.pop()

# Initialise a stack
# s = Stack()

# Push an item to the stack s
# s.push(1)

# Pop an item from the stack s
# s.pop()