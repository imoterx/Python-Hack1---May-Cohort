class QueueWithStacks:
    def __init__(self):
        self.stack_in = []  # Stack to handle enqueue operations
        self.stack_out = [] # Stack to handle dequeue operations

    def enqueue(self, x: int):
        # Push element onto stack_in
        self.stack_in.append(x)

    def dequeue(self) -> int:
        # If stack_out is empty, transfer all elements from stack_in to stack_out
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        # If stack_out is still empty, raise an error (queue is empty)
        if not self.stack_out:
            raise IndexError("dequeue from an empty queue")
        
        # Pop and return the top element from stack_out
        return self.stack_out.pop()
