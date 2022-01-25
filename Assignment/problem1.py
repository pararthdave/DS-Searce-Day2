
class Stack: 
    def __init__(self):
        # We are using an empty list for creating stack 
        self.stack = []

    # Check if the stack is empty or not 
    def isEmpty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False

    # This function returns the top element of the stack 
    def top(self):
        return self.stack[-1]

    def st_push(self, val):
        self.stack.append(val)

    def st_pop(self):
        if self.isEmpty():
            return "Stack is empty. Unserflow!"
        else:
            return self.stack.pop()
    def getMax(self):
        max=self.stack[0]
        for i in self.stack:
            if i>max:
                max=i
        return max


s = Stack()
s.st_push(1)
s.st_push(2)
s.st_push(7)
s.st_push(4)
s.st_push(10)

print("Popped",s.st_pop())
print("Maximum",s.getMax())