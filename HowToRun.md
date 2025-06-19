TrueCaller Spam Detector and Contact Search API
===============================================

How to Run the Project
----------------------

---

### 1\. Set Up the Environment

- Ensure you have **Python 3.8 or higher** installed.
- Create a **virtual environment**:

  `python -m venv venv`
- Activate the virtual environment:

  - **Windows**:

    `venv\Scripts\activate`
  - **macOS/Linux**:

    `source venv/bin/activate`

---

### 2\. Install Dependencies

- Install all required packages using `pip`:

  `pip install -r requirements.txt`

---

### 3\. Configure the Database

- Make sure **PostgreSQL** is installed and running.
- Update the `DATABASES` settings inside your `settings.py` file with your PostgreSQL credentials:

  `DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'your_database_name', 'USER': 'your_database_user', 'PASSWORD': 'your_database_password', 'HOST': 'localhost', 'PORT': '5432', } }`

---

### 4\. Run Migrations

- Apply the migrations to set up the database schema:

  `python manage.py migrate`

---

### 5\. Create a Superuser (Admin)

- Create a Django superuser to manage users from the admin panel:

  `python manage.py createsuperuser`

---

### 6\. Run the Development Server

- Start the Django server:

  `python manage.py runserver`
- Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

API Endpoints 🚀
----------------

All API requests require authentication using a **JWT Access Token**.

### 1\. Authentication

- **Obtain Token**:

  - URL: `POST /api/token/`
  - Body (JSON):

    `{ "username": "your_superuser_username", "password": "your_superuser_password" }`
  - Response:

    `{ "refresh": "your-refresh-token", "access": "your-access-token" }`
- **Refresh Token**:

  - URL: `POST /api/token/refresh/`
  - Body (JSON):

    `{ "refresh": "your-refresh-token" }`

### 2\. Test Endpoint

- **Check Authentication**:

  - URL: `GET /test/`
  - Headers:

    `Authorization: Bearer <access_token>`

### 3\. Register User

- **Register or Update a User**:

  - URL: `POST /register/`
  - Body (JSON):

    `{ "phone_number": "9876543210", "name": "John Doe", "email_address": "john@example.com" }`

### 4\. Call User

- **Log a Call Event**:

  - URL: `POST /call/`
  - Body (JSON):

    `{ "phone_number": "9876543210" }`

### 5\. Report Spam

- **Report a Number as Spam**:

  - URL: `POST /spam/`
  - Body (JSON):

    `{ "phone_number": "9876543210" }`

### 6\. Search Users

- **Search by Name or Phone Number**:

  - URL: `GET /search/`
  - Query Parameters:

    - `query`: Search term (name or phone number)
    - `email` *(optional)*: Your email address to fetch related contacts
  - Example:

    `GET /search/?query=john&email=your_email@example.com`

---

Important Notes ⚡
------------------

- **Authorization**: All API calls must have the header:

  `Authorization: Bearer <your-access-token>`
- **Postman / curl**: You can test the API easily with tools like **Postman** or **curl**.
- **User Creation**: Initially, create a superuser to obtain the token.
- **Spam Likelihood Calculation**:

  - After each `call` or `spam` report, the `spam_likelihood` is updated automatically.
