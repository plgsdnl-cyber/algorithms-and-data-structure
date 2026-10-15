class Deque:
    def __init__(self):
        self.data = []

    def append_left(self, item):
        self.data.insert(0, item)

    def append_right(self, item):
        self.data.append(item)

    def pop_left(self):
        if self.data:
            return self.data.pop(0)
        return None

    def pop_right(self):
        if self.data:
            return self.data.pop()
        return None

    def size(self):
        return len(self.data)