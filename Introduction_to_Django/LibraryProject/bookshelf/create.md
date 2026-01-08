rom bookshelf.models import Book

# Create and save the book in one step
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
print(book)

# Output:
1984 by George Orwell