# NumSight📞🔍 – Intelligent Caller ID & Spam Detection API
A Django-based backend system for phone number resolution, spam detection, and intelligent caller identification using REST APIs.

---

## 🚀 Overview

**NumSight** is a modular backend platform that combines custom Django ORM models, scalable REST APIs, and real-time data ingestion pipelines to identify callers, detect spam, and return relevant caller metadata. Designed to mimic core features of platforms like Truecaller, it enables intelligent name-to-number mapping and spam classification at scale.

---

## ✨ Features

- 🔗 **Caller ID Lookup** – Reverse search functionality by name or number.
- 📊 **Call & Spam Reporting** – Endpoints to log call events and report numbers as spam, which automatically updates spam likelihood.
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

### 1. Clone the repo and Set Up Virtual Environment
It's highly recommended to use a virtual environment.
```bash
python -m venv venv
```
Activate the virtual environment:
- Windows :
```bash
.\venv\Scripts\activate
```
- maxOS/Linux :
```bash
source venv/bin/activate
```

### 2. Install Dependencies
With your virtual environment activated, install all required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Configure Database
Ensure your PostgreSQL server is running. Create a new database for the project (e.g., numsight_db).

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

### 3. Run migrations and populate data
Apply database migrations to set up the schema and then populate initial data using the provided script.
```bash
python manage.py migrate
python populate_data.py
```

### 4. Create a Superuser (Admin)
Create a Django superuser to access the admin panel and obtain JWT tokens for API testing:
```bash
python manage.py createsuperuser
```
Follow the prompts to set your username, email, and password.


### 5. Start the development server
```bash
python manage.py runserver
```
The API will now be accessible at http://127.0.0.1:8000/.




## 🔌 API Endpoints

Here are some key endpoints (JWT auth required for protected routes):

| Method | Endpoint               | Description                           |
|--------|------------------------|---------------------------------------|
| GET    | `/test`                | Verify token validity.                |
| GET    | `/api/search/`         | Search contact by name or number      |
| POST   | `/api/token/`          | Get access & refresh JWT tokens       |
| POST   | `/api/token/refresh/`  | Refresh JWT access token              |
| GET    | `/api/protected/`      | Example protected endpoint            |

| Method | Endpoint                    | Description                                                                             | Body/Query Params Example                                        |
| :----- | :-------------------------- | :---------------------------------------------------------------------------------------| :--------------------------------------------------------------- |
| `GET`  | `/test/`                    | Simple authenticated endpoint to verify token validity.                                 | -                                                                |
| `POST` | `/api/token/`               | Get access & refresh JWT tokens                                                         | -                                                                |
| `POST` | `/api/token/refresh/`       | Refresh JWT access token                                                                | -                                                                |
| `POST` | `/register/`                | Register a new `GlobalUser` or update an existing one (e.g., add name/email).           | `{"phone_number": "9876543210", "name": "John Doe", "email_address": "john@example.com"}` |
| `POST` | `/call/`                    | Log a call event for a phone number. Increments `total_appearance` & `spam_likelyhood`. | `{"phone_number": "9988776655"}`                                 |
| `POST` | `/spam/`                    | Report a phone number as spam. Increments `num_spam` & `spam_likelyhood`.               | `{"phone_number": "9988776655"}`                                 |
| `GET`  | `/search/`                  | Search contacts by name or phone number.                                                | `?query=Alice&email=your_email@example.com`                      |

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

```markfile
 - by **Karansinh Rathod** > Feel free to reach out or connect!
```
