#metodos magicos

class Book:
    def __init__(self,title,author, num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        #return self.num_pages + other.num_pages
        return f"{self.num_pages + other.num_pages} paginas"

    def __contains__(self, keyword):
        #return keyword in self.title
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return  f" key {key} is not found"



book1 = Book("as aranhas","H.P.L.",310)
book2 = Book("Parry Hotter e a rochinha no rim","Joker rolinha",220)
book3 = Book("o leao, a bruxa e o movel","lelio",172)
book4 = Book("as aranhas","H.P.L.",310)

print(book1)
print(book2)
print(book3)
print(book1==book2)
print(book1==book4)
print(book1<book4)
print(book2 + book3)
print("leao" in book3)
print("leao" in book2)
print("Joker" in book2)
print("Joker" in book4)
print(book1 ['title'])
print(book1 ['author'])
print(book1 ['num_pages'])
print(book3 ['num_pages'])
print(book3 ['3'])



