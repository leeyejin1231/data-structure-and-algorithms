class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

    def get_data(self):
        return self.value
    
    def get_next(self):
        return self.pointer

    def set_data(self, newdata):
        self.value = newdata

    def set_next(self, newpointer):
        self.pointer = newpointer