class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(s: str) -> str:
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.push(char)
    
    # Pop all characters from the stack and form the reversed string
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str
