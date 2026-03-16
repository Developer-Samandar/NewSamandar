# NewSamandar

Django project for managing posts (blog or shop).

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Go to the Backend folder: `cd Backend`
6. Apply migrations: `python manage.py migrate`
7. Run the server: `python manage.py runserver`

## Usage

- Home page: /
- List of posts: /posts/
- Create post: /create-posts/
- Post details: /post/<id>/
- Edit post: /post/<id>/edit/
- Delete post: /post/<id>/delete/

## Project Structure

- `Backend/`: Main Django application
- `online_shop/`: App for posts
- `templates/`: HTML templates
- `static/`: Static files (CSS, JS)

## Model

The `Post` model with fields:
- title: Title
- content: Content
- created_at: Creation date
- updated_at: Update date