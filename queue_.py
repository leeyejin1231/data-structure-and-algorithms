class Queue(object):
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not bool(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            value = self.items[0]
            del self.items[0]
            return value
        else:
            return "Queue is empty."

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[0]
        else:
            return "Queue is empty."
    
    def __repr__(self):
        return repr(self.items)
    
if __name__ == "__main__":
    queue = Queue()
    print(f"큐가 비었나요? {queue.is_empty()}")
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐 크기: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"큐가 비었나요? {queue.is_empty()}")
    print(queue)