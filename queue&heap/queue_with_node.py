class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer # 새로운 거 저장

class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        return not bool(self.count)
    
    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.pointer
            self.count -= 1
            return value
        else:
            return "Queue is empty."

    def enqueue(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.pointer = node
            self.tail = node
        self.count += 1
    
    def size(self):
        return self.count

    def peek(self):
        return self.head.value

    def _print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()
        

if __name__ == "__main__":
    queue = LinkedQueue()
    print(f"큐가 비었나요? {queue.is_empty()}")
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐가 비었나요? {queue.is_empty()}")
    queue._print()

    print(f"큐 크기: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    queue._print()