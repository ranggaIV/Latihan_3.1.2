class Queue:
    def __init__(self):
        self.queue = []
    # enqueue menambahkan elemen ke akhir list 
    def enqueue(self, item):
        self.queue.append(item)
    #dequeue mengambil elemen pertama dari list
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    #peek mengambil elemen pertama dari list tanpa menghapusnya
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    #is_empty digunakan untuk memeriksa apakah antrian kosong atau tidak.
    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


class MainQueue:
    def queueExample(self):
        queue = Queue()
        queue.enqueue("Java")
        queue.enqueue("DotNet")
        queue.enqueue("PHP")
        queue.enqueue("HTML")
        print("remove", queue.dequeue())
        print("element", queue.peek())
        print("poll:", queue.dequeue())
        print("peek:", queue.peek())

    def main(self):
        self.queueExample()


if __name__ == "__main__":
    MainQueue().main()