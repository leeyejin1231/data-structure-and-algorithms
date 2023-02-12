class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        value = self.items.pop()
        if self.items:
            return value
        else:
            return "Stack is empty."

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return "Stack is empty."
    
    def __repr__(self):
        return repr(self.items)


if __name__ == "__main__":
    stack = Stack()
    print(f"스택이 비었나요? {stack.is_empty()}")
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    print(f"스택 크기: {stack.size()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"스택이 비었나요? {stack.is_empty()}")
    print(stack)