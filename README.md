# Expence-Tracker

# 💰 Expense Tracker

A simple and beginner-friendly Full Stack Expense Tracker built to help developers learn Frontend, Backend, Database Management, REST APIs, and GitHub Collaboration.

---

## 📌 Project Overview

Expense Tracker is a web application that allows users to record their income and expenses, monitor their spending habits, and track their current balance.

This project is designed for students and beginner developers who want practical experience building a complete Full Stack application.

---

# 🎯 Objectives

- Learn Git and GitHub collaboration
- Understand REST API development
- Practice Database Design
- Connect Frontend and Backend
- Implement CRUD Operations
- Learn Software Development Workflow
- Experience Team Collaboration

---

# ✨ Features

## Income Management
- Add Income
- View Income History
- Update Income Records
- Delete Income Records

## Expense Management
- Add Expenses
- View Expense History
- Update Expense Records
- Delete Expense Records

## Dashboard
- Total Income
- Total Expenses
- Current Balance
- Transaction Summary

## Search and Filter
- Search Transactions
- Filter by Income
- Filter by Expense
- Filter by Date

---

# 🛠 Technology Stack

## Frontend
- HTML5
- CSS3
- JavaScript (ES6)

## Backend
- Python
- FastAPI

## Database
- SQLite

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
expense-tracker/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── docs/
│   └── api_documentation.md
│
├── screenshots/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🗄 Database Design

## Transactions Table

| Column | Type | Description |
|----------|----------|----------|
| id | Integer | Primary Key |
| title | String | Transaction Name |
| amount | Float | Transaction Amount |
| type | String | Income or Expense |
| date | Date | Transaction Date |

---

# 🔌 API Endpoints

## Create Transaction

```http
POST /transactions
```

Request Body:

```json
{
  "title": "Salary",
  "amount": 500000,
  "type": "Income"
}
```

---

## Get All Transactions

```http
GET /transactions
```

---

## Get Transaction By ID

```http
GET /transactions/{id}
```

---

## Update Transaction

```http
PUT /transactions/{id}
```

---

## Delete Transaction

```http
DELETE /transactions/{id}
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/dottomtundu9-MTUNDU/Expense-tracker.git
```

Move into project folder:

```bash
cd expense-tracker
```

---

# ⚙ Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend Setup

Open:

```text
frontend/index.html
```

or use:

```bash
python -m http.server 5500
```

---

# 👥 Team Collaboration Workflow

## Step 1

Fork Repository

## Step 2

Clone Repository

```bash
git clone repository-url
```

## Step 3

Create Branch

```bash
git checkout -b feature-name
```

Examples:

```bash
git checkout -b frontend-ui
git checkout -b backend-api
git checkout -b database-design
```

## Step 4

Commit Changes

```bash
git add .
git commit -m "Added new feature"
```

## Step 5

Push Changes

```bash
git push origin feature-name
```

## Step 6

Create Pull Request

Submit Pull Request on GitHub.

---

# 📋 Project Roles

## Backend Developer

Responsibilities:

- API Development
- Business Logic
- Validation
- Database Integration

---

## Frontend Developer

Responsibilities:

- UI Design
- Forms
- Dashboard
- API Integration

---

## Database Developer

Responsibilities:

- Database Design
- Schema Management
- Data Validation

---

## QA Tester

Responsibilities:

- Test Features
- Report Bugs
- Verify Fixes
- Documentation

---

# 📝 Future Improvements

- User Authentication
- JWT Security
- Monthly Reports
- Graphs and Charts
- Export PDF Reports
- Dark Mode
- Multi-User Support
- Mobile Responsive Design

---

# 🎓 Learning Outcomes

By completing this project, contributors will learn:

- Git Fundamentals
- GitHub Collaboration
- Branching Strategy
- Pull Requests
- Code Reviews
- Frontend Development
- Backend Development
- API Design
- Database Management
- Software Engineering Best Practices

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create your branch
3. Commit changes
4. Push changes
5. Open Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you find this project useful:

- Star the repository
- Share with friends
- Contribute improvements

Happy Coding 🚀
