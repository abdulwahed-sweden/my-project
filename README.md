# Django Authentication and Profile System

A complete Django authentication system with extended user profiles, password reset functionality, and Bootstrap 5 UI.

## Features

- User registration with email
- Login and logout
- Extended user profiles with:
  - Profile pictures (avatars)
  - Biography
  - Location
  - Birth date
- Complete password management:
  - Password change for logged-in users
  - Password reset via email
- Responsive Bootstrap 5 UI
- Form validation and error handling
- Flash messages for user feedback

## Project Structure

```
backend/
├── users/                  # User authentication app
│   ├── migrations/
│   ├── templates/
│   │   └── users/          # User-related templates
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   │       ├── profile.html
│   │       ├── edit_profile.html
│   │       ├── password_change.html
│   │       ├── password_change_done.html
│   │       ├── password_reset.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_confirm.html
│   │       └── password_reset_complete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py            # Forms for user registration and profile
│   ├── models.py           # Profile model
│   ├── urls.py             # URL patterns for authentication
│   └── views.py            # View functions
├── core/                   # Core app for main pages
│   ├── templates/
│   │   └── pages/
│   │       └── home.html
│   ├── urls.py
│   └── views.py
├── templates/              # Project-level templates
│   └── base.html
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

## Setup Instructions

1. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install required packages**

```bash
pip install django pillow
```

3. **Configure email settings for password reset**

Add the following to your `settings.py`:

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your email provider's SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'  # Use app password for Gmail
```

4. **Configure media settings for profile pictures**

Add the following to your `settings.py`:

```python
# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

5. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Access the application**

Navigate to:
- http://127.0.0.1:8000/ - Home page
- http://127.0.0.1:8000/users/register/ - Registration
- http://127.0.0.1:8000/users/login/ - Login
- http://127.0.0.1:8000/users/profile/ - User profile (requires login)

## Customization

### Custom User Model (Optional)

If you want to use a custom User model, define it in `users/models.py` and set `AUTH_USER_MODEL = 'users.CustomUser'` in `settings.py` before running migrations.

### Additional Profile Fields

To add more fields to the Profile model:

1. Update `users/models.py` to add new fields to the Profile model
2. Update `users/forms.py` to include the new fields in the ProfileUpdateForm
3. Update the profile templates to display the new fields
4. Run migrations to apply the changes

### Email Templates

Password reset emails use the default Django templates. To customize them, create the following template files:

- `templates/registration/password_reset_email.html`
- `templates/registration/password_reset_subject.txt`

## Using Social Authentication (Optional Extension)

To add social authentication (Google, Facebook, etc.), you can integrate Django Allauth:

1. Install Django Allauth:
```bash
pip install django-allauth
```

2. Configure it in `settings.py` following the Django Allauth documentation.

## Security Notes

- In production, make sure `DEBUG = False`
- Use environment variables for sensitive settings
- Configure HTTPS for secure data transmission
- Review Django's deployment checklist
