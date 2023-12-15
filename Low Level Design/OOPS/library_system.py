# Users can create libraries and add their favourite books

class User:
    USER_ID = 0

    def __init__(self, name):
        self.id = User.USER_ID
        User.USER_ID += 1
        self.name = name
        self.library = Library()

    def __str__(self):
        return str({"name": self.name, "library": str(self.library)})


class Library:
    def __init__(self):
        self.collection = dict()

    def add_book(self, book):
        self.collection[book.id] = book

    def remove_book(self, book_id):
        del self.collection[book_id]

    def __str__(self):
        s = ""
        for i in self.collection:
            s += str(self.collection[i]) + ", "
        # returns string without ", " in the end    
        return s[:len(s)-2]


class Book:
    BOOK_ID = 0

    def __init__(self, title, author, content):
        self.id = Book.BOOK_ID
        Book.BOOK_ID += 1
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return str(self.title)


if __name__ == "__main__":
    book1_title = "The Alchemist"
    book1_content = ["page_1", "page_2", "page_3"]
    book1_author = "Paulo Coelho"
    book1 = Book(book1_title, book1_author, book1_content)
    book2_title = "Rich Dad Poor Dad"
    book2_content = ["page_1", "page_2", "page_3"]
    book2_author = "Robert Kiyosaki"
    book2 = Book(book2_title, book2_author, book2_content)
    user1 = User("user1")
    user1.library.add_book(book1)
    user1.library.add_book(book2)
    print(user1)
