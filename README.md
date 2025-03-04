# A Django Authentication System

## Overview
Auth is a Django-based user authentication system that provides user registration, email verification, login, and logout functionalities. 
It includes token-based email verification and user session handling.

## Features
- User Registration
- Email Verification using Token
- Secure User Authentication (Login & Logout)
- Session Handling
- Flash Messages for User Feedback
- Django Messages Framework Integration

## Installation
## 1. Clone the Repository
git clone https://github.com/mnesh01/Auth.git
cd Auth

## 2. Create a Virtual Environment 
python -m venv env
source env/bin/activate  # On Mac/Linux
env\Scripts\activate  # On Windows

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Configure Environment Variables
Create a .env file in the root directory and add:

## 5. Apply Migrations
python manage.py migrate

## 5. Run the server
python manage.py runserver
