class Stack:
    def __init__(self):
        self.stack = []

    def pull(self):
        index = len(self.stack) - 1
        ret = self.stack[index]
        del self.stack[index]
        return ret

    def push(self, item):
        self.stack += [item]
        return self.stack

    def get(self, index):
        return self.stack[index]


class Queue:
    def __init__(self):
        self.queue = []

    def pull(self):
        index = 0
        ret = self.queue[index]
        del self.queue[index]
        return ret

    def push(self, item):
        self.queue += [item]
        return self.queue

    def get(self, index):
        return self.queue[index]


stack = Stack()

pushItems = input('Items to push').split()
for item in pushItems:
    stack.push(item)
print(stack.pull())

queue = Queue()
pushItems = input('Items to push').split()
for item in pushItems:
    queue.push(item)
print(queue.pull())

