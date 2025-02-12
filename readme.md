# Django Project: Polls and Blog

## Overview
This is a Django-based web application that includes two main apps:
- **Polls**: A simple polling app where users can vote on questions.
- **Blog**: A blogging app where users can read and manage articles.
- **User Authentication**: Includes a login page for user authentication.

## Features
- User authentication (Login required for some views)
- Polls app for creating and voting on polls
- Blog app for reading and managing blog posts
- Admin panel for managing content

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure the Database
```sh
python manage.py migrate
```

### 5. Create a Superuser (for Admin Panel)
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6. Run the Development Server
```sh
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

## Directory Structure
```
my_project/
│── blog/            # Blog application
│── polls/           # Polls application
│── my_project/      # Django project settings
│── templates/       # HTML templates
│── static/          # Static files (CSS, JS, images)
│── db.sqlite3       # SQLite database (default)
│── manage.py        # Django management script
│── requirements.txt # List of dependencies
│── docs/            # Documentation (Sphinx)
```

## API Documentation
To generate API documentation using Sphinx, follow these steps:
```sh
cd docs
make html
```
Then, open `docs/build/html/index.html` in a web browser.
