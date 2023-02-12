class Heapify(object):
    def __init__(self, data = None):
        self.data = data or []
        
    def __repr__(self):
        return repr(self.data)

    def parent(self, i):

    def left_child(self, i):

    def right_child(self, i):

    def __max_heapify__(self, i):
    
    def extract_max(self):
    
    def insert(self, item):

def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print("테스트 통과!")

if __name__ == "__main__":
    test_heapify()