# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):
    oldest_book = book1.year

    if oldest_book == book2.year:
        result = f"{book1.name} and {book2.name} were published in {oldest_book}"
        print(result)
    elif oldest_book < book2.year:
        result = f"{book1.name} is older, it was printed in {oldest_book}"
        print(result)
    else:
        result = f"{book2.name} is older, it was printed in {book2.year}"
        print(result)
    

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, norma)