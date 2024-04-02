# HW1_P2: Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement
'''
You are maintaining a library system where each book is stored as a tuple 
within a list. Your task is to update this system by adding new books and 
ensuring no duplicates.

- Add functionality to insert new books into library.
- Ensure that adding a duplicate book is handled appropriately.
'''
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(title, author):
    book = (title, author)
    if book in library:
        print(f"Sorry this book can not be added, '{book}' already is in the library.")
    else:
        library.append(book)
        print(f"Yay! '{book}' has been added successfully!")

print(library)
add_book("The Alchemist", "Paulo Coelho")
add_book("1984", "George Orwell")
print(library)
