# Django ToDo App

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A simple ToDo application built with Django that allows users to create, manage, and track their tasks.

## Features

- User authentication (Register, Login, Logout)
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Simple and intuitive user interface
- Responsive design

## Prerequisites

- Python 3.x
- Django 4.x
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahin07m/django_todo.git
   cd django_todo
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
django_todo/
├── todo/                      # Main app directory
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Database models
│   ├── urls.py                # App URL routes
│   ├── views.py               # App views
│   └── ...
├── todoproject/               # Project configuration
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project URL routes
│   └── ...
├── manage.py                  # Django management script
└── requirements.txt           # Project dependencies
```

## Docker Setup (Simple Version)

### Quick Start
1. Make sure you have Docker installed
2. Run these commands:

```bash
docker-compose up --build
```

3. Open your browser:  
   `http://localhost:8000`

### Basic Commands
- Start: `docker-compose up`
- Stop: `docker-compose down`
- Create admin user:  
  `docker-compose exec web python manage.py createsuperuser`

### Files Needed
Just add these 2 files to your project:

1. `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements
CMD python manage.py runserver 0.0.0.0:8000
```


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, please contact:

Mahin - [GitHub Profile](https://github.com/Mahin07m)

---
