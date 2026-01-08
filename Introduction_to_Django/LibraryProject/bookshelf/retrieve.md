from bookshelf.models import Book

```python
# Get the book object
book = Book.objects.get(title="1984")

# Display attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Year: {book.publication_year}")

# Output:
Title: 1984
Author: George Orwell
Year: 1949