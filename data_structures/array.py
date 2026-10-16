class MyArray:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def insert(self, index, item):
        self.data.insert(index, item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("индекс вне рамок")

    def size(self):
        return len(self.data)
