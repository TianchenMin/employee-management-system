# Employee Management System

A Django-based web application for managing employees, tracking attendance, and visualizing data with a modern dashboard. The system provides a RESTful API for integration and a Chart.js-powered dashboard for real-time insights.

## Features

- **Employee Management:** Add, update, and manage employee records and departments.
- **Attendance Tracking:** Record and monitor employee attendance with status (Present, Absent, Late).
- **Performance Reviews:** Track employee performance ratings over time.
- **REST API:** Full-featured API for all core resources, with filtering and authentication.
- **Dashboard:** Interactive dashboard visualizing attendance statistics using Chart.js.

## Tech Stack

- **Backend:** Django, Django REST Framework, django-filter
- **Frontend:** HTML, Chart.js
- **Database:** SQLite (default, easily swappable)
- **Authentication:** Token-based (DRF)
- **API Docs:** Swagger/OpenAPI via drf-yasg

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd employee-management-system
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django djangorestframework django-filter drf-yasg
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Dashboard: [http://localhost:8000/api/dashboard/](http://localhost:8000/api/dashboard/)
   - API Root: [http://localhost:8000/api/](http://localhost:8000/api/)

### Project Structure

```
employee-management-system/
├── employees/         # Employee, Department, Attendance, Performance models & APIs
├── attendance/        # (Optional) Additional attendance logic
├── employee_project/  # Project settings and URLs
├── templates/         # Dashboard HTML (Chart.js)
├── manage.py
└── db.sqlite3
```

## REST API

All endpoints require token authentication.

| Resource      | Endpoint                        | Methods      | Description                |
|---------------|---------------------------------|--------------|----------------------------|
| Departments   | `/api/departments/`             | CRUD         | Manage departments         |
| Employees     | `/api/employees/`               | CRUD         | Manage employees           |
| Attendance    | `/api/attendance/`              | CRUD         | Track attendance           |
| Performance   | `/api/performance/`             | CRUD         | Employee performance       |
| Dashboard     | `/api/dashboard/`               | GET          | Attendance dashboard (UI)  |

- Filtering is available on most endpoints (e.g., `?department=1`, `?status=P`).
- API documentation (Swagger): `/swagger/` (if enabled in URLs).

## Dashboard

The dashboard (`/api/dashboard/`) visualizes attendance statistics using Chart.js. It fetches attendance data from the API and displays counts of Present, Absent, and Late statuses in a bar chart.

## Models Overview

- **Department:** `name`
- **Employee:** `name`, `email`, `phone_number`, `address`, `date_of_joining`, `department`
- **Attendance:** `employee`, `date`, `status` (Present, Absent, Late)
- **Performance:** `employee`, `rating` (1-5), `review_date`

## Authentication

- Obtain a token via DRF's token authentication.
- Include the token in the `Authorization` header for API requests:
  ```
  Authorization: Token <your-token>
  ```

## Development

- To add new features, create a branch and submit a pull request.
- Run tests with:
  ```bash
  python manage.py test
  ```

## License

[MIT](LICENSE) (or your preferred license) 