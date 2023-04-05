#Latihan 1
class Stack:
    #self.stack untuk menampung elemen-elemen pada stack
    def __init__(self):
        self.stack = []
    #push() menambahkan elemen ke dalam list pada posisi terakhir
    def push(self, item):
        self.stack.append(item)
    #pop() menghapus elemen terakhir dari list dan mengembalikan nilai
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    #peek() mengambil nilai elemen terakhir dari list tanpa menghapusnya
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    #is_empty() digunakan untuk memeriksa apakah stack kosong atau tidak
    def is_empty(self):
        return len(self.stack) == 0
    #search() digunakan untuk mencari indeks elemen pada stack, dimulai dari ujung stack.
    def search(self, item):
        try:
            index = self.stack.index(item)
        except ValueError:
            return -1
        return len(self.stack) - index

    def __str__(self):
        return str(self.stack)


class Prototype:
    def main(self):
        at = Stack()
        at.push("Aku")
        at.push("Anak")
        at.push("Indonesia")

        print("Next :", at.peek())
        at.push("Raya")
        print(at.pop())
        at.push("!")

        count = at.search("Aku")
        while count != -1 and count > 1:
            at.pop()
            count -= 1
        print(at.pop())
        print(at.is_empty())


if __name__ == "__main__":
    Prototype().main()
