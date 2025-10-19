# 🐱 Profile API — Stage Zero Backend Task (HNG)

A small Django REST API that returns user information, the current UTC timestamp, and a random cat fact fetched from the Cat Facts API (https://catfact.ninja/fact).

---

## 🚀 Endpoint

GET /me

Replace the example deployment URL below with your actual deployed URL when sharing:

https://your-app.example.com/me

---

## 🧩 Example Response

```json
{
  "status": "success",
  "user": {
    "email": "your_email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T09:45:30.456Z",
  "fact": "Cats sleep for around 13 to 14 hours a day."
}
```

## Quick start (Windows terminal)

Open terminal, then:

```terminal
git clone https://github.com/jerahmeel200/Dynamic-Profile-Endpoint.git
cd profile-api
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver
# Visit: http://127.0.0.1:8000/me
```

If you're using Command Prompt (cmd.exe) on Windows, activate the venv with:

```cmd
venv\Scripts\activate.bat
```

## Quick start (macOS / Linux)

```bash
git clone https://github.com/<your-username>/profile-api.git
cd profile-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
# Visit: http://127.0.0.1:8000/me
```

## Project structure

Top-level layout for this repo:

profile-api/
├── api/            # app containing the /me endpoint
│   ├── views.py
│   ├── urls.py
│   └── __init__.py
├── project/        # Django project settings and entry points
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
