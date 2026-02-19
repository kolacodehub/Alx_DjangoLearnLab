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