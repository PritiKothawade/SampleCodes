class Library(object):

    def __init__(self, books_dict):
        self.books_dictionary = books_dict

    def display_books(self):
        print("Books available are: ")
        for book in self.books_dictionary.keys():
            if self.books_dictionary.get(book) > 0:
                print(book)

    def process_borrow_books(self, book_name):
        # check availability
        if self.books_dictionary.get(book_name, 0) > 0:
            print("Congrats! Book is available!")
            # update count
            self.books_dictionary[book_name] -= 1
        else:
            print("Oops Books is not available!")

    def update_return_books(self, book_name):
        if self.books_dictionary.get(book_name):
            self.books_dictionary[book_name] += 1
        else:
            print("Book no from library")


if __name__ == '__main__':
    books_dictionary = {'ABC': 2, 'DEF': 2}
    lb = Library(books_dictionary)
    lb.display_books()
    lb.process_borrow_books('ABC')
    lb.display_books()
    lb.process_borrow_books('ABC')
    lb.display_books()
    lb.process_borrow_books('ABC')
    lb.update_return_books('ABC')
    lb.display_books()
    lb.process_borrow_books('FGH')
    lb.update_return_books('FGH')