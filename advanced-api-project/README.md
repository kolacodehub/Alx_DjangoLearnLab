# Advanced API Project - Book Management

This API provides a comprehensive system for managing a book collection, built with Django REST Framework.

## View Configurations & Endpoints

| Endpoint | Method | View Class | Permission | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/api/books/` | GET | `BookListView` | Public | List all books. |
| `/api/books/<int:pk>/` | GET | `BookDetailView` | Public | View book details. |
| `/api/books/create/` | POST | `BookCreateView` | Authenticated | Create a new book. |
| `/api/books/edit/<int:pk>/` | GET/PUT | `BookUpdateView` | Authenticated | Edit a book (Pre-populated). |
| `/api/books/delete/<int:pk>/` | DELETE | `BookDeleteView` | Authenticated | Delete a book. |

## Custom Behavior & Hooks
- **Data Pre-population**: The `BookUpdateView` utilizes `RetrieveUpdateAPIView`. This ensures that when a user accesses the edit page via a GET request, the existing data is returned, allowing for an intuitive editing experience.
- **Save Hooks**: The `BookCreateView` implements `perform_create` to allow for future expansion, such as automatically assigning the book creator or triggering notifications.
- **Future Validation**: The `BookSerializer` (referenced by these views) includes a custom validator to prevent `publication_year` from being set in the future.

## Permissions Logic
The API follows the **"Read-Only for Public"** standard. While the catalog is open for viewing (`AllowAny`), all write operations (`POST`, `PUT`, `DELETE`) are protected by `IsAuthenticated` to prevent unauthorized data modification.

## Advanced Query Features

The `/books/` endpoint supports advanced filtering, searching, and sorting options.

### 1. Filtering (Exact Match)
Filter the list by specific field values.
- **URL Parameter:** `?<field_name>=<value>`
- **Example:** Get all books published in 2024.
  `GET /api/books/?publication_year=2024`
- **Example:** Get all books by a specific Author ID.
  `GET /api/books/?author=3`

### 2. Searching (Text Search)
Perform a text search across Book titles and Author names.
- **URL Parameter:** `?search=<term>`
- **Example:** Find books with "Harry" in the title or author name.
  `GET /api/books/?search=Harry`

### 3. Ordering (Sorting)
Sort the results by specific fields. Use a `-` prefix for descending order.
- **URL Parameter:** `?ordering=<field_name>`
- **Example:** Sort by publication year (Newest first).
  `GET /api/books/?ordering=-publication_year`
- **Example:** Sort alphabetically by title.
  `GET /api/books/?ordering=title`

### 4. Combined Usage
You can combine all three parameters for complex queries.
- **Example:** Search for "Fantasy" books, published in 2023, ordered by title.
  `GET /api/books/?search=Fantasy&publication_year=2023&ordering=title`