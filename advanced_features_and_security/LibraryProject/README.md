# Authentication and Permissions Setup

## Custom User Model

This project uses a custom user model (`CustomUser`) defined in `users.models`.

- **Fields:** Adds `date_of_birth` and `profile_photo` to the standard Django user.
- **Manager:** Uses `CustomUserManager` to handle user creation with these new fields.

## Permission System

We utilize Django's Group and Permission system to enforce Role-Based Access Control (RBAC).

### Defined Permissions

The `Article` model defines four custom permissions in its `Meta` class:

1. `can_view`: Allows reading article content.
2. `can_create`: Allows creating new articles.
3. `can_edit`: Allows updating existing articles.
4. `can_delete`: Allows removing articles.

### User Roles (Groups)

Permissions are assigned to Groups, not users directly.

1. **Viewers**: Has `can_view`.
2. **Editors**: Has `can_view`, `can_create`, and `can_edit`.
3. **Admins**: Has all permissions including `can_delete`.

### How to Enforce

Views use the `@permission_required` decorator:

```python
@permission_required('users.can_create', raise_exception=True)
def article_create(request):
    ...
```
# Security Enhancements Documentation

## 1. Secure Settings (settings.py)
- **DEBUG = False**: Disables detailed error pages in production to prevent leaking sensitive configuration data.
- **SECURE_BROWSER_XSS_FILTER**: Enables the browser's XSS filtering.
- **X_FRAME_OPTIONS = 'DENY'**: Prevents the site from being embedded in iframes, stopping Clickjacking attacks.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Prevents the browser from MIME-sniffing a response away from the declared content-type.
- **CSRF/SESSION_COOKIE_SECURE**: Ensures cookies are only transmitted over HTTPS connections.

## 2. Content Security Policy (CSP)
- Implemented via custom middleware (`ContentSecurityPolicyMiddleware`).
- **Policy**: `default-src 'self'` restricts resources (scripts, styles, images) to load only from the same origin, mitigating XSS risks.

## 3. Secure Views & Input Handling
- **SQL Injection Prevention**: All database queries use the Django ORM (`.filter()`, `.get()`), which automatically parameterizes inputs. Raw SQL queries are avoided.
- **CSRF Protection**: All POST forms include the `{% csrf_token %}` tag.