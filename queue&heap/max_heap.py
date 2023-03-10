class Heapify(object):
    def __init__(self, data = None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)
        
    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i % 2 == 1:
            return i // 2
        else:
            return i // 2 - 1

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def __max_heapify__(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        if left < n:
            if self.data[left] > self.data[i]:
                largest = left
        if right < n:
            if self.data[right] > self.data[largest]:
                largest = right

        if i != largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.__max_heapify__(largest)
    
    def extract_max(self):
        max = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.__max_heapify__(0)
        return max
    
    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item


def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print("테스트 통과!")

if __name__ == "__main__":
    test_heapify()