class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[-1]
            del self.stack[-1]
        else:
            return -1
        return popped_element

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return -1

    def size(self):
        return len(self.stack)


class Queue(Stack):

    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()

    def push(self, data):
        self.enqueue.push(data)

    def move_to_dequeue(self):
        while not self.enqueue.is_empty():
            self.dequeue.push(self.enqueue.pop())

    def pop(self):
        if self.dequeue.is_empty():
            self.move_to_dequeue()
        return self.dequeue.pop()


class Queue1(Stack):
    def __init__(self):
        super(Queue1, self).__init__()

    def popRec(self):
        if self.size() == 1:
            return self.pop()

        item = self.pop()
        dequeued_item = self.popRec()
        self.push(item)
        return dequeued_item


if __name__ == "__main__":

    q = Queue1()
    q.push(10)
    q.push(20)
    q.push(40)
    q.push(5)
    q.push(6)
    q.push(60)
    print(q.popRec())
    print(q.popRec())
    print(q.popRec())
    print(q.popRec())
    q.push(90)
    print(q.popRec())
    print(q.popRec())
    print(q.popRec())

