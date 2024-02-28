└── flask_auth_app
    └── project
        ├── __init__.py       # setup the app
        ├── auth.py           # the auth routes for the app
        ├── views.py          # the views routes for the app
        ├── db.sqlite         # the database -> will automatically created
        ├── models.py         # the user model
        ├── main.py           # the app runner
        └── templates
            ├── base.html     # contains common layout and links
            ├── index.html    # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            └── signup.html   # Show the signup form

Step 1 - Installing Packages
- Create the project directory: $ mkdir flask_auth_app
- Navigate to the project directory: $ cd flask_auth_app
- Create the project folder $ mkdir project
- Navigate to the project directory: $ cd project
- Install the needed packages: $ pip install flask flask-sqlalchemy flask-login

Step 2 - Creating the App Files
        ├── __init__.py       # setup the app
        ├── auth.py           # the auth routes for the app
        ├── views.py          # the views routes for the app
        ├── db.sqlite         # the database -> will automatically created
        ├── models.py         # the user model
        ├── main.py           # the app runner
        └── templates
            ├── base.html     # contains common layout and links
            ├── index.html    # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            └── signup.html   # Show the signup form

Step 3 - Adding Routes
        ├── auth.py           # the auth routes for the app
        ├── views.py          # the views routes for the app

Step 4 - Creating Templates
        └── templates
            ├── base.html     # contains common layout and links
            ├── index.html    # show the home page
            ├── login.html    # show the login form
            ├── profile.html  # show the profile page
            └── signup.html   # Show the signup form

Step 5 - Creating User Models
        ├── db.sqlite         # the database -> will automatically created
        ├── models.py         # the user model

Step 6 - Configuraiotn the Database
        ├── __init__.py       # setup the app

Step 7 - Setting up the Authorization Function
Step 8 - Testing Sign Up Method
Step 9 - Adding the Login Method
Step 10 - Protecting Pages
