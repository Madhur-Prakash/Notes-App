# 📝 Note-Taking App

A lightweight and extensible **Flask-based note-taking web application** that includes:

- User authentication (Sign up, Log in, Log out)
- Note creation, update, and deletion
- Templated front-end with HTML + JS
- SQLite database using **SQLAlchemy**
---

## 🚀 Features

- 🔐 **User Authentication**  
  Sign-up and login functionality with session management.

- 🗒️ **Note Management**  
  Create, update, and delete personal notes.

- 🧩 **Modular Code Structure**  
  Separation of concerns with `views`, `models`, and `auth`.

- ⚙️ **ORM with SQLAlchemy**  
  SQLite-backed persistence using SQLAlchemy.


---

## Technology Stack
- **Backend Framework**: Flask
- **Database**: SQLAlchemy
- **Password Hashing**: werkzeug
- **Programming Language**: Python

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/Notes-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Notes-App
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up MongoDB:
   - Install MongoDB and start the service.
   - Configure the MongoDB URI in the `.env` file.

---

## Usage

1. Start the FastAPI server:
   ```bash
   python app.py
   ```
2. Access the API at:
   ```
   http://127.0.0.1:5000/
   ```
   ---


## 📁 Project Structure

```plaintext
note-taking/
├── .gitignore  # gitignore file for GitHub
├── Dockerfile
├── Readme.md
├── app.py  # main FastAPI app
├── instance
│   └── notes.db
├── requirements.txt
└── website
    ├── __init__.py  # initializes package
    ├── auth.py
    ├── models.py  # models
    ├── static
    │   └── index.js
    ├── templates
    │   ├── base.html
    │   ├── home.html
    │   ├── login.html
    │   ├── sign-up.html
    │   └── update.html
    └── views.py
```
---

## Future Enhancements
---

- 🧠 **User Profile Page**  
  Let users update their profile info (name, email, avatar).

- 📅 **Reminder and Scheduling**  
  Add due dates and notifications for notes.

- 🌙 **Dark Mode Toggle**  
  Improve UX with light/dark theme support.

- 🔍 **Search and Filter**  
  Search notes by title or content, and filter by creation/update date.

- 🏷️ **Tagging and Categories**  
  Organize notes using custom tags or categories.


- 📊 **Dashboard & Analytics**  
  Track note activity, count, and user insights.

- 🔐 **Two-Factor Authentication (2FA)**  
  Add optional 2FA for extra security.


- 🧭 **Role-Based Access Control (RBAC)**  
  Allow for admin and regular user roles for better user management.

---

## Contribution Guidelines

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

## Author
**Madhur Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)

---

