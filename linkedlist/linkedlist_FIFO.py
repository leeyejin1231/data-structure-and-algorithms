from node import Node

class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    
    def _print(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

    def _add_first(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def _delete_first(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")

    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    def add_node(self, value):
        if not self.head:
            self._add_first(value)
        else:
            self._add(value)

    def _find(self, index):
        return

    def _find_by_value(self, value):
        return

    def delete_node(self, index):
        return

    def delete_node_by_value(self, value):
        return


if __name__ == "__main__":
    ll = LinkedListFIFO()
    for i in range(1, 5):
        ll.add_node(i)
    print("연결 리스트 출력:")
    ll._print()
    print("인덱스가 2인 노드 삭제 후, 연결 리스트 출력:")
    ll.delete_node(2)
    ll._print()
    print("값이 15인 노드 추가 후, 연결 리스트 출력:")
    ll.add_node(15)
    ll._print()
    print("모든 노드 모두 삭제 후, 연결 리스트 출력:")
    for i in range(ll.length-1, -1, -1):
        ll.delete_node(i)
    ll._print()