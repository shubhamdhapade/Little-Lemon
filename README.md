# 🍋 Little Lemon Restaurant Website

A full-stack restaurant web application built using **Django** as part of the **Meta Back-End Developer Professional Certificate**. The project demonstrates Django fundamentals including models, views, templates, URL routing, forms, the Django Admin panel, static files, and SQLite database integration.

## ✨ Features

- 🏠 Home, About, Booking, Menu, and Menu Item pages
- 🍽️ Dynamic menu generated from the database
- 📄 Individual menu item details with descriptions and images
- 📅 Online reservation booking form
- 💾 SQLite database integration
- 🔧 Django Admin panel for managing menu items and reservations
- 🎨 Responsive UI with static assets (CSS & images)
- 🧩 Template inheritance and reusable partials
- 🔗 Dynamic URL routing using primary keys
- 📂 Django ORM for database operations

## 🛠️ Tech Stack

- Python 3
- Django
- HTML5
- CSS3
- SQLite
- Django Template Language (DTL)

## 📁 Project Structure

```
littlelemon/
│
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── restaurant/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Learning Outcomes

This project demonstrates practical experience with:

- Django Models
- Django Views
- Django Templates
- Template Inheritance
- Django Forms
- Static Files
- URL Routing
- Django Admin
- SQLite Database
- CRUD Operations
- Dynamic Web Pages

## Installation

```bash
git clone https://github.com/yourusername/Little-Lemon.git

cd Little-Lemon

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

## Screenshots

- Home Page
- Menu Page
- Menu Item Page
- Booking Page
- Django Admin Dashboard

## Course

Developed as part of the **Meta Back-End Developer Professional Certificate** on Coursera.
