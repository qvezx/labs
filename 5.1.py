class book:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

a = str(input("Введите название книги: "))
b = str(input("Введите автора книги: "))
c = int(input("Введите год издания: "))

book1 = book(a, b, c)

book1.get_info()
        