from bookshelf.models import Book

**Python Command:**
```python
# 1. Fetch the updated book
book = Book.objects.get(title="Nineteen Eighty-Four")

# 2. Delete it
book.delete()

# 3. Confirm deletion by checking all books
all_books = Book.objects.all()
print(all_books)

# Output:
(1, {'my_app.Book': 1})
<QuerySet []> 
# Note: The empty QuerySet [] confirms the database is empty (or this specific book is gone).