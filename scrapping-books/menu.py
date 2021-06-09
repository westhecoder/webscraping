from app import books

USER_CHOICE = ''' Enter one of the following
     -'b' to look at 5-start books
     -'c' to look at the cheapest books
     -'n' to just get the next available books on the catalogue
     -'q' to exit
     Enter your choice: '''



def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating)[:10]
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


#print_best_books()
#print('----- CHEPEST BOOKS-------')
#print_cheapest_books()
user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
        user_input = input(USER_CHOICE)
        while user_input != 'q':
            if user_input in ('b', 'c', 'n'):
                user_choices[user_input]()
            else:
                print('Pleaes choose a valid command.')
            user_input = input(USER_CHOICE)

menu()
