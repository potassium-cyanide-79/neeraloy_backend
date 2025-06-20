[![Backend CI](https://github.com/potassium-cyanide-79/neeraloy_backend/actions/workflows/ci.yml/badge.svg)](https://github.com/potassium-cyanide-79/neeraloy_backend/actions/workflows/ci.yml)

# Neeraloy Backend

This is the React-based frontend for the Neeraloy home rental and roommate matching platform.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/potassium-cyanide-79/neeraloy_backend.git
cd neeraloy_backend
```

### 2. Install dependencies

```bash
python -m venv n_venv
source n_venv/bin/activate   # for macOS/Linux
n_venv\Scripts\activate      # for Windows
```

### 3. Start the development server

```bash
pip install -r requirements.txt
```

### 4. Start the development server

Create a .env file and add your settings (example):
```bash
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:pass@localhost:5432/neeraloy_db
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Running Tests

```bash
python pytest
```

neeraloy_backend/ <br>
│                 <br> 
├── api/ <br>
├── tests/  
├── manage.py     <br>
├── requirements.txt <br>
└── README.md        <br>