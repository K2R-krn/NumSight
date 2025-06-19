# NumSight 🔍  
A Django-based backend system for phone number resolution, spam detection, and intelligent caller identification using REST APIs.

---

## 🚀 Overview

**NumSight** is a modular backend platform that combines custom Django ORM models, scalable REST APIs, and real-time data ingestion pipelines to identify callers, detect spam, and return relevant caller metadata. Designed to mimic core features of platforms like Truecaller, it enables intelligent name-to-number mapping and spam classification at scale.

---

## ✨ Features

- 🔗 **Caller ID Lookup** – Reverse search functionality by name or number.
- 🚫 **Spam Detection** – Flags spam-marked numbers using query-based detection logic.
- 🔍 **Optimized Querying** – High-performance DB lookups via `Q` objects and indexed fields.
- 🧠 **LLM-Driven Agent Support** – (Optional integration) for enhanced query handling.
- 📦 **Custom Data Ingestion** – Bulk data population via Python scripts with deduplication.
- 🔐 **JWT Authentication** – Secured API access using DRF and `SimpleJWT`.

---

## 🧰 Tech Stack

| Layer        | Tech                                      |
|--------------|-------------------------------------------|
| Backend      | Python, Django, Django REST Framework     |
| Database     | PostgreSQL                                |
| Scraping     | BeautifulSoup, Selenium                   |
| LLM Agents   | LangChain, OpenAI API (for advanced logic)|
| Frontend     | Streamlit (for chatbot demo)              |
| Auth         | JWT (`djangorestframework-simplejwt`)     |

---
## ⚙️ Setup Instructions

### 1. Clone the repo and Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Make sure PostgreSQL is running and the database is created.

### 3. Run migrations and populate data
```bash
python manage.py migrate
python populate_data.py
```

### 4. Start the development server
```bash
python manage.py runserver
```



## 🔌 API Endpoints

Here are some key endpoints (JWT auth required for protected routes):

| Method | Endpoint               | Description                           |
|--------|------------------------|---------------------------------------|
| GET    | `/api/search/`         | Search contact by name or number      |
| POST   | `/api/token/`          | Get access & refresh JWT tokens       |
| POST   | `/api/token/refresh/`  | Refresh JWT access token              |
| GET    | `/api/protected/`      | Example protected endpoint            |

📌 **Add Header:**

```makefile
Authorization: Bearer <access_token>
```


## 🧠 Future Enhancements

- ✅ **Swagger/OpenAPI documentation**
- ✅ **Admin interface for spam management**
- 🚀 **Docker support for deployment**
- 🔄 **Redis-based caching for frequent lookups**
- 📈 **Analytics dashboard for usage stats**

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

- by **Karansinh Rathod**
> Feel free to reach out or connect!

