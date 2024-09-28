Basic E-commerce Website using Flask and SQLAlchemy

Here is a simulated screenshot of the e-commerce website:

Home Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)

Hero section with a call-to-action (CTA) button to view products

Featured products section with a grid layout


Footer with copyright information and social media links

Product List Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)

Product list with a grid layout

Each product card includes:

Product image

Product name

Product price

Add to cart button

Pagination links at the bottom of the page

Product Edit Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)

Product edit form with the following fields:

Product name

Product price

Product description

Save changes button

Order List Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)

Order list with a table layout

Each order row includes:

Order ID

Customer name

Order date

Total amount

View order button

Order View Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)

Order details with the following information:

Order ID
Customer name
Order date
Total amount
Product list with quantity and price
Customer List Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)
Customer list with a table layout
Each customer row includes:
Customer ID
Customer name
Email address
View customer button
Customer View Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)
Customer details with the following information:
Customer ID
Customer name
Email address
Address
Registration Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)
Registration form with the following fields:
Name
Email address
Password
Confirm password
Register button
Login Page:

Header with navigation menu (Products, Orders, Customers, Register, Login)
Login form with the following fields:
Email address
Password
Login button

This is a basic e-commerce website built using Flask and SQLAlchemy. It includes features such as product listing, product editing, product deletion, order management, customer management, registration, and login.
FEATURES:
Product listing with pagination
Product editing and deletion
Order management with order listing and order viewing
Customer management with customer listing and customer viewing
Registration and login functionality
Basic user authentication and authorization
Technologies Used:

Flask: A micro web framework for Python
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python
Bootstrap: A popular front-end framework for building responsive and mobile-first websites
HTML: HyperText Markup Language for structuring and presenting content on the web
CSS: Cascading Style Sheets for styling and layout
JavaScript: A high-level, dynamic, and interpreted programming language for client-side scripting
Database:

SQLite: A self-contained, file-based relational database

A fully functional e-commerce website with product listing, order management, customer management, registration, and login functionality.
Code:

The code for this project is provided in the above files.

Please note that you need to run the Flask application by executing the app.py file to access these pages.

Here are the steps to run the Flask application:

Open a terminal or command prompt.
Navigate to the directory where you have saved the app.py file.
Type python app.py to run the Flask application.
Open a web browser and navigate to http://localhost:5000/ to access the home page of the e-commerce website.
Note: Make sure you have Flask and Flask-SQLAlchemy installed in your Python environment. You can install them using pip:

pip install flask flask-sqlalchemy
