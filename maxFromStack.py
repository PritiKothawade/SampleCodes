class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            print("Popped", self.stack[-1])
            del self.stack[-1]
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1


class MaxStack(Stack):

    def __init__(self):
        self.cur_stack = Stack()
        self.max_stack = Stack()

    def push(self, data):
        self.cur_stack.push(data)
        max_till_now = self.max_stack.peek()
        if data > max_till_now:
            self.max_stack.push(data)
        else:
            self.max_stack.push(max_till_now)

    def get_max(self):
        return self.max_stack.peek()


if __name__ == "__main__":

    ms = MaxStack()
    ms.push(10)
    ms.push(20)
    ms.push(40)
    ms.push(5)
    ms.push(6)
    ms.push(60)
    print(ms.get_max())
