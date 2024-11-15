# Permissions and Groups Setup in Django

## Overview
This project includes a detailed setup for using Django's groups and permissions to control access to parts of the application.

### Custom Permissions
- Added custom permissions to the `Article` model in `models.py`.
- Permissions include `can_view`, `can_create`, `can_edit`, and `can_delete`.

### Groups Configuration
- **Editors**: Can create and edit articles.
- **Viewers**: Can view articles.
- **Admins**: Full access to create, edit, view, and delete articles.

### Enforcing Permissions
- Views are protected using the `@permission_required` decorator to ensure only users with appropriate permissions can access certain actions.

### How to Test
1. Create test users and assign them to the relevant groups.
2. Log in as these users and verify that permissions are enforced correctly by accessing the views.

### Management Command
Run the setup script to create and assign permissions:
```bash
python manage.py setup_permissions
