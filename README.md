# CMS Authentication System

A Django-based authentication system developed as part of an NGO CMS Internship Project.  
This system provides secure user registration, login, password reset, and admin management.



## Features

- User Registration  
- User Login & Logout  
- Password Reset via Email  
- Secure Authentication (Django default)  
- Admin Panel for Managing Users  
- Deployed Live using Render 

## Live Project URL

https://ngo-auth.onrender.com

##  Technologies Used

- Python 3.10  
- Django 5  
- SQLite Database  
- HTML & CSS  
- Render (Cloud Hosting)  
- GitHub (Version Control)  

##  How It Works

1. A user registers using the registration form.
2. Their details are stored securely in the database.
3. The user can log in using their username and password.
4. If the password is forgotten, the user can reset it via email.
5. Admins can view and manage users using Django Admin Panel.

##  Project Structure

ngo_auth/
│
├── accounts/ # User authentication app
├── templates/ # HTML pages (login, register, reset, etc)
├── db.sqlite3 # Database
├── manage.py
└── requirements.tx

## Installation (For Local Use)

1. Clone the repository  
git clone https://github.com/SAUMAYJ13/ngo-auth.git

2. Go inside the folder  
cd ngo-auth

3. Install dependencies  
pip install -r requirements.txt

4. Run migrations  
python manage.py migrate

5. Run the server  
python manage.py runserver

6. Open in browser  
http://127.0.0.1:8000


##  Admin Panel

To create admin account:

python manage.py createsuperuser

Then visit:  
/admin


## Internship Use

This project demonstrates:
- Web authentication
- Database handling
- Secure login system
- Deployment on cloud
- Real-world Django workflow


Saumay Jadhav  
Internship Project – NGO CMS Authentication System
