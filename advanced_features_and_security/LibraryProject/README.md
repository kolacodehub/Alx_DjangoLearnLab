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
