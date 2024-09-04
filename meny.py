from app import books

USER_CHOISE = """Enter one of the following

-b to look 5 start books
-c to look cheapest books
-n to just get next book from the catalouge
-q to exit.
"""

def print_best_books():
    best_books = sorted(books, key= lambda x : x.rating*-1)[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_book = sorted(books, key= lambda x : x.price)[:10]
    for book in cheapest_book:
        print(book)

book_generator = (x for x in books )
def get_next_book():
    print(next(book_generator))

user_choise = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
    user_input = input(USER_CHOISE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choise[user_input]()
        else:
            print('Please enter valid character!')
        user_input = input(USER_CHOISE)

menu()