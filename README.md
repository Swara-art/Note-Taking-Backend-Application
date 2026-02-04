# 📝 Note Taking Backend Application

A RESTful backend service for a Note-Taking Application built using **FastAPI** and **MongoDB**.  
This application allows users to create, read, update, and delete notes efficiently using CRUD APIs.

The project is designed with a modular structure, proper request validation, and clean API design, making it suitable for learning backend development and for use as a portfolio project.

---

## 🚀 Features

- Create a new note
- Retrieve all notes
- Retrieve a note by ID
- Update an existing note
- Delete a note
- MongoDB document-based storage
- Automatic API documentation using Swagger UI

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Backend Framework:** FastAPI  
- **Database:** MongoDB  
- **Database Driver:** PyMongo  
- **API Style:** REST  
- **Validation:** Pydantic  

---

## 📁 Project Structure

app/
├── main.py
├── routes/
│ ├── create.py
│ ├── read.py
│ ├── update.py
│ ├── delete.py
│ └── init.py
├── data/
│ ├── database.py
│ ├── schema.py
│ └── init.py


---

## 📡 API Endpoints

| Method | Endpoint            | Description              |
|------|---------------------|--------------------------|
| POST | `/notes`            | Create a new note        |
| GET  | `/notes`            | Get all notes            |
| GET  | `/notes/{note_id}`  | Get note by ID           |
| PUT  | `/notes/{note_id}`  | Update a note            |
| DELETE | `/notes/{note_id}` | Delete a note            |

---

## 📄 Note Schema

Each note contains the following fields:

- `id` (string)
- `title` (string)
- `content` (string)
- `created_at` (datetime)
- `updated_at` (datetime)

---

## ▶️ How to Run the Project
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Swara-art/Note-Taking-Backend-Application
```

### 2️⃣ Create a virtual environment
```
-python -m venv venv
-source venv/bin/activate
```

### 3️⃣ Install dependencies
```
-pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI server
```
-uvicorn main: app --reload
```

### 📘 API Documentation
```
-Once the server is running, open your browser and visit:
-Swagger UI:
-http://127.0.0.1:8000/docs
```

### 👩‍💻 Author

-Swara Deshpande
-Computer Science Student
-Backend Developer (FastAPI, MongoDB)

### 📜 License

This project is for educational purposes.
---

