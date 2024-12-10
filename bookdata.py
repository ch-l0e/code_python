class Book:
    def __init__(self, title, author, pages, year, text_type):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.text_type = text_type
    
    def info(self):
        return f"Book(title: {self.title} author: {self.author} pages: {self.pages} year: {self.year} text type: {self.text_type})"
    
b1 = Book("why cats are cool", "francis", 105, 1986, "non fiction")
print(b1.info())