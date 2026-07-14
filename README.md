# Simple FastAPI Task Manager API

## Project Description

This project is a simple Task Manager REST API built using Python and FastAPI.

It allows users to:

- Add a Task
- View All Tasks
- Update a Task
- Delete a Task

The application uses SQLite as the database, SQLAlchemy as the ORM, and Pydantic for request validation.

---

## Technologies Used

- Python 3
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

---

## Project Structure

```
task_manager/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── README.md
└── tasks.db
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Move to the project folder

```bash
cd task_manager
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Add Task

POST `/tasks`

### View All Tasks

GET `/tasks`

### Update Task

PUT `/tasks/{id}`

### Delete Task

DELETE `/tasks/{id}`

---

## Sample JSON

```json
{
    "title": "Balaji",
    "description": "Python Developer",
    "status": "Pending"
}
```

---

## Database

Database: SQLite

Database File:

```
tasks.db
```

Table Name:

```
tasks
```

Columns:

- id
- title
- description
- status

---

## Author

Balaji M