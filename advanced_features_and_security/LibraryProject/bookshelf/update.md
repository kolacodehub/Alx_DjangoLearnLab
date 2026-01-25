from bookshelf.models import Book

```python
# 1. Fetch the book
book = Book.objects.get(title="1984")

# 2. Update the attribute
book.title = "Nineteen Eighty-Four"

# 3. Save to database
book.save()

# 4. Verify the update
print(book.title)

# Output:
Nineteen Eighty-Four