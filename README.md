# Employee Management REST API

A production-ready REST API built with Django and Django REST Framework for managing employees and companies. Features JWT authentication, advanced filtering, search capabilities, and auto-generated Swagger documentation.

## 🚀 Features

- **JWT Authentication** — Secure login/logout with access and refresh tokens
- **Company Management** — Full CRUD with employee count per company
- **Employee Management** — Complete CRUD with advanced filters and search
- **Search & Filters** — Filter by company, status, department, gender
- **Auto Documentation** — Swagger UI and ReDoc available out of the box
- **Clean Architecture** — Serializers, ViewSets, and Routers properly structured

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- SimpleJWT
- drf-yasg (Swagger)
- django-filter
- SQLite (easily switchable to PostgreSQL)

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/Corzito/employee-management-api.git
cd employee-management-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install django djangorestframework djangorestframework-simplejwt drf-yasg django-filter

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## �API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/login/ | Get JWT token |
| POST | /api/auth/refresh/ | Refresh JWT token |

### Companies
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/companies/ | List all companies |
| POST | /api/companies/ | Create company |
| GET | /api/companies/{id}/ | Get company detail |
| PUT | /api/companies/{id}/ | Update company |
| DELETE | /api/companies/{id}/ | Delete company |

### Employees
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/employees/ | List all employees |
| POST | /api/employees/ | Create employee |
| GET | /api/employees/{id}/ | Get employee detail |
| PUT | /api/employees/{id}/ | Update employee |
| DELETE | /api/employees/{id}/ | Delete employee |
| GET | /api/employees/active/ | List active employees |
| GET | /api/employees/by_company/ | Filter by company |

## 📖 Documentation

Once the server is running, visit:
- **Swagger UI:** http://127.0.0.1:8000/swagger/
- **ReDoc:** http://127.0.0.1:8000/redoc/

## 🔐 Authentication Example
```bash
# Get token
POST /api/auth/login/
{
  "username": "admin",
  "password": "yourpassword"
}

# Use token in requests
Authorization: Bearer <your_access_token>
```

## 👨‍💻 Author

**Andres Corzo**  
Backend Developer — Django & Python  
GitHub: [@Corzito](https://github.com/Corzito)
