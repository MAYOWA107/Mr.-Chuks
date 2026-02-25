# Mr.-Chuks
Mr. Chuks — Food Management API

Mr. Chuks is a backend project built with Django and Django REST Framework.
It provides a REST API (a set of web addresses) that allows a food business to manage food items, user accounts, orders, and image uploads.

This project is designed to help developers or businesses build food-ordering systems and easily connect it with a frontend app (like a website or mobile app).



This backend API lets you:

Manage Users
  a. Create new user accounts
  b. Log in users securely
  c. Authenticate users before they use protected features

Manage Food Items(By admin)
  a. Add new food items
  b. View all food items(everyone can see this)
  c. Update details of food items
  d. Delete food items
  e. Upload images for food items

Manage Orders
  a. Create new orders
  b. View all orders
  c. Track orders

All these actions are done through simple web addresses called endpoints that return data in JSON format.

“CRUD functionality” means you can Create, Read, Update, and Delete data.

This project uses:
  a. Python & Django — The main language and framework
  b. Django REST Framework — Makes building APIs easier
  c. SQLite — A simple database (stored locally)
  d. Image Upload Support — You can attach food pictures


How to Run (Basic Steps)

Clone the repository
  a. git clone https://github.com/MAYOWA107/Mr.-Chuks.git

Install dependencies
  a. pip install -r requirements.txt

Create environment variables
  a. Create a file called .env with secret keys and database settings.

Run the server
  a. python manage.py runserver

Open your API in a browser or API tool like Postman.



API Documentation (Swagger)

This project includes interactive API documentation using Swagger.

Swagger provides a simple web page where you can:
  a. View all available API endpoints
  b. See what each endpoint does
  c. Enter data and test the API directly from the browser
  d. Check responses instantly
  
You don’t need any special tools like Postman — everything can be tested in one place using swagger.

How to Access Swagger?

After running the server, open your browser and go to:

http://127.0.0.1:8000/swagger/
