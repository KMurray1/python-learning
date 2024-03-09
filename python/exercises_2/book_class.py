class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} published in the year {self.publication_year}"
    
book = Book('Harry Potter', 'JK Rowling', 2000)
print(book)