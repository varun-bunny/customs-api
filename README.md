# Customs Customer & Branch API 🚀

A fully working Dockerized REST API for managing customers and their branches.  
Built with FastAPI, PostgreSQL, Docker Compose, and SQLAlchemy.

## 🌐 Live Swagger Docs
Once running, go to: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ⚙️ Tech Stack
- FastAPI
- PostgreSQL
- Docker Compose
- SQLAlchemy ORM
- Pydantic validation

---

## 🧪 API Endpoints

### Customers
- `GET /customers` – List all
- `POST /customers` – Create
- `GET /customers/{cust_id}` – View
- `DELETE /customers/{cust_id}` – Delete

### Branches
- `POST /branches` – Create
- `GET /branches` – List
- `GET /branches/{branch_id}` – View

---

## 🐳 Setup Instructions (Docker)

```bash
git clone https://github.com/YOUR_USERNAME/customs-api.git
cd customs-api
docker compose up --build

