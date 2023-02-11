class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer # 이전 거 저장

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            return "Stack is empty."

    def peek(self):
        if self.count:
            return self.head.value
        else:
            return "Stack is empty."

    def size(self):
        return self.count

    def _print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

if __name__ == "__main__":
    stack = Stack()
    print(f"스택이 비었나요? {stack.isEmpty()}")
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    stack._print()
    print(f"스택 크기: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"스택이 비었나요? {stack.isEmpty()}")
    stack._print()
