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