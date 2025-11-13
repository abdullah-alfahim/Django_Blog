# Django Blog

A Django-based blogging application with user authentication and blog management.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/abdullah-alfahim/Django_Blog.git
cd Django_Blog
```

### 2. Create Virtual Environment

```bash
python3 -m venv myenv
```

### 3. Activate Virtual Environment

**On Linux/macOS:**
```bash
source myenv/bin/activate
```

**On Windows:**
```bash
myenv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install Django==5.2.3
pip install Pillow==11.2.1
pip install sqlparse
```

```

## Running the Django Server

### 1. Navigate to the Project Directory

```bash
cd blog
```

### 2. Apply Database Migrations

```bash
python manage.py migrate
```

### 3. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

### Server Output

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 13, 2025 - 20:57:24
Django version 5.2.3, using settings 'blog.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Accessing the Application

- **Main App:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Sign Up:** http://127.0.0.1:8000/accounts/signup/
- **Log In:** http://127.0.0.1:8000/accounts/login/

## Stopping the Server

Press **CONTROL-C** in the terminal where the server is running.

## Project Structure

```
blog/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── accounts/                # User authentication app
├── config/                  # Blog configuration app
├── core/                    # Core app
├── blog/                    # Main project settings
├── templates/               # HTML templates
└── media/                   # User-uploaded media files
```

## Notes

- The development server auto-reloads when you modify Python files
- Use `CONTROL-C` to stop the server
- This is a development server only; use a production WSGI/ASGI server for deployment
- For more information: https://docs.djangoproject.com/en/5.2/howto/deployment/
