# Django Custom Auth API

A robust Django REST Framework (DRF) backend featuring a fully customized user model, token-based authentication, and profile management with image upload capabilities.

## 🚀 Features

* **Custom User Model:** Extends `AbstractUser` with `bio`, `profile_picture`, and a symmetrical `followers` system.
* **Token Authentication:** Secure login/logout using DRF's Token Authentication.
* **Profile Management:**
    * **Register:** Create an account with username, email, and password.
    * **Login:** Retrieve an auth token + user details.
    * **Profile:** View and update profile details (Bio & Picture).
    * **Logout:** Securely invalidate the authentication token.

## 🛠️ Tech Stack

* Python 3.x
* Django 5.x
* Django REST Framework
* Pillow (Image Processing)

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <your-project-folder>
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install django djangorestframework pillow
    ```

4.  **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

## 🔑 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/auth/register/` | Create a new user account | ❌ No |
| `POST` | `/api/auth/login/` | Get Token & User Info | ❌ No |
| `GET` | `/api/auth/profile/` | View current user profile | ✅ Yes (Token) |
| `PATCH` | `/api/auth/profile/` | Update bio or upload picture | ✅ Yes (Token) |
| `POST` | `/api/auth/logout/` | Invalidate current token | ✅ Yes (Token) |

## 🧪 How to Test (Postman / Thunder Client)

1.  **Register:** Send a `POST` to `/register/` with JSON body:
    ```json
    {
      "username": "johndoe",
      "email": "john@example.com",
      "password": "securepassword123"
    }
    ```

2.  **Login:** Send a `POST` to `/login/` with credentials. Copy the `token` from the response.

3.  **Access Protected Routes:**
    * For `/profile/` or `/logout/`, go to the **Headers** tab.
    * Key: `Authorization`
    * Value: `Token <your_copied_token_here>`

## 📸 Media Files
User uploads (profile pictures) are stored in the `media/profile_pics/` directory. Ensure your `settings.py` is configured to serve media files during development.


<!-- --------------------------- -->

📝 Posts & Comments API Documentation
Base URL: http://127.0.0.1:8000/api/
Authentication: All write operations (POST, PUT, PATCH, DELETE) require a valid token passed in the header: Authorization: Token <your_token>.

1. Posts Endpoints
List All Posts
Endpoint: GET /posts/

Auth Required: No

Query Parameters (Optional):

?page=2 (Pagination)

?search=keyword (Search title and content)

?author=1 (Filter by exact author ID)

Success Response (200 OK):

JSON
{
    "count": 50,
    "next": "http://127.0.0.1:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "saedaan",
            "title": "Learning DRF",
            "content": "ViewSets and Routers make life so much easier!",
            "comments": [],
            "created_at": "2026-02-20T10:00:00Z",
            "updated_at": "2026-02-20T10:00:00Z"
        }
    ]
}
Create a Post
Endpoint: POST /posts/

Auth Required: Yes

Request Body:

JSON
{
    "title": "My New Post",
    "content": "This is the content of my post."
}
Success Response (201 Created): Returns the created post object.

Retrieve a Single Post
Endpoint: GET /posts/<id>/

Auth Required: No

Success Response (200 OK): Returns the single post object, including any nested comments.

Update a Post
Endpoint: PUT /posts/<id>/ (or PATCH for partial updates)

Auth Required: Yes (Must be the author)

Request Body (PATCH example):

JSON
{
    "content": "I am updating just the content of this post."
}
Success Response (200 OK): Returns the updated post object.

Delete a Post
Endpoint: DELETE /posts/<id>/

Auth Required: Yes (Must be the author)

Success Response (204 No Content): Returns nothing upon successful deletion.

2. Comments Endpoints
List All Comments
Endpoint: GET /comments/

Auth Required: No

Success Response (200 OK):

JSON
{
    "count": 120,
    "next": "http://127.0.0.1:8000/api/comments/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 5,
            "author": "saedaan",
            "content": "Great post!",
            "created_at": "2026-02-20T11:05:00Z",
            "updated_at": "2026-02-20T11:05:00Z"
        }
    ]
}
Create a Comment
Endpoint: POST /comments/

Auth Required: Yes

Request Body:

JSON
{
    "post": 5, 
    "content": "I completely agree with this."
}
Success Response (201 Created): Returns the created comment object.

Retrieve, Update, or Delete a Comment
Retrieve: GET /comments/<id>/ (No auth required)

Update: PATCH /comments/<id>/ (Requires Token, must be author)

Delete: DELETE /comments/<id>/ (Requires Token, must be author)

<!-- ---------------------------------- -->
🤝 Social & Feed API Documentation
These endpoints handle the social graph (following/unfollowing users) and generating the personalized timeline feed.

Authentication: All endpoints in this section require a valid token passed in the header: Authorization: Token <your_token>.

1. Social Endpoints (Follow/Unfollow)
Follow a User
Endpoint: POST /auth/follow/<user_id>/

Auth Required: Yes

URL Parameter: user_id (The integer ID of the user you want to follow)

Request Body: None required.

Success Response (200 OK):

JSON
{
    "message": "You are now following saedaan"
}
Error Response (400 Bad Request): Triggered if you try to follow yourself.

JSON
{
    "error": "You cannot follow yourself."
}
Error Response (404 Not Found): Triggered if the user_id does not exist in the database.

Unfollow a User
Endpoint: POST /auth/unfollow/<user_id>/

Auth Required: Yes

URL Parameter: user_id (The integer ID of the user you want to unfollow)

Request Body: None required.

Success Response (200 OK):

JSON
{
    "message": "You have unfollowed saedaan"
}
2. Personalized Feed Endpoint
Get User Feed
Endpoint: GET /feed/
(Note: If you placed this inside posts/urls.py, the full URL might be /api/feed/ or /api/posts/feed/ depending on your main config/urls.py routing)

Auth Required: Yes

Description: Returns a paginated list of all posts written by the users that the currently authenticated user is following.

Ordering: Posts are ordered by created_at in descending order (newest first).

Success Response (200 OK):

JSON
{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/feed/?page=2",
    "previous": null,
    "results": [
        {
            "id": 42,
            "author": "saedaan",
            "title": "My first post for my followers!",
            "content": "This will only show up in the feed of people who follow me.",
            "comments": [],
            "created_at": "2026-02-20T12:00:00Z",
            "updated_at": "2026-02-20T12:00:00Z"
        },
        {
            "id": 38,
            "author": "another_user",
            "title": "Django is awesome",
            "content": "Building APIs is getting easier every day.",
            "comments": [
                {
                    "id": 5,
                    "author": "saedaan",
                    "content": "I agree completely!",
                    "created_at": "2026-02-20T11:45:00Z"
                }
            ],
            "created_at": "2026-02-20T10:30:00Z",
            "updated_at": "2026-02-20T10:30:00Z"
        }
    ]
}