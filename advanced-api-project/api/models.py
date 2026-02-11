from django.db import models

class Author(models.Model):
    """
    Represents a book author in the system.
    
    Purpose: To store the primary identity of writers. This model 
    acts as the 'parent' in a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents an individual book entry.
    
    Purpose: To store specific details about a book, including its title 
    and publication year. Each book is linked to exactly one Author.
    
    Relationship Logic:
    - The ForeignKey creates a Many-to-One relationship (Many books, one Author).
    - 'related_name="books"' allows us to access an author's books from the 
      Author instance (e.g., author.books.all()).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title