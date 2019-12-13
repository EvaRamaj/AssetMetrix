# AssetMetrix

**Requirements:**

    1. python3.6
    2. flask (pip install flask)
    3. flask forms (pip install flask-wtf)
    4. flask_login(pip install flask-login)
    5. sqlalchemy(pip install flask-sqlalchemy)

**Launch application:**

    At the directory of the application run the file: main.py

**Structure Description:**

    The core components of the structure of this application are
    
    AssetMetrix/
        application/
        statics/
        templates/
        main.py
        database.py

The directory "templates" contains html files which define the layout for each page in our application.

The directory "statics" contains information that is stored in the database and load every time, such us the custon css that we apply to the layouts, the images, etc.

The directory "application" contains all the core dynamic components such us the fields of each form and the schema of our database.

The file database.py contains a function which is called on main.py and initializes the database and the application.

Finally, the main file is were we define the routes and initialize our database.application.


**Application description:**

  As soon as the user enters the homepage of the application we check if this user is already logged in 
  or not. (For example, if he has been logged in a different tab on the browser).
  If the user has not been logged in jet, the login page is loaded. On this page the user has two options:

      1. Fill the form entering his name and password:
     
  The user has to fill his username and password, these fields are both validated in the database 
  and if the user has entered something wrong (either on username or password), an error message 
  will appear which indicates the wrong username or password.
  After the successful login the user is redirected to a custom homepage where he/she can see a 
  custom welcoming message. On this page the user has an additional ability to logout from the system.

      2. Follow the registration link:
      
  This link redirects to the registration form. On this form the user has to fill the username,
  email and password twice. All the fields are required and if the user does not fill any of them, 
  an error message will appeared. In addition, for the **username** , **e-mail** and **password** 
  more validations have been implemented.
  More specifically, for the e-mail we check if the format is correct and follows the requirements 
  of an e-mail address (someone@domain.com). Moreover we check if the e-mail address or the username 
  already exist in our database (in case of existence the user is prompted to use a different one).
  On the other hand, for the password, we first check if the password's length is less than 8 characters, 
  in this case again an error message is appeared which indicated that a longer password should be filled.
  Secondly, we check if the fields "password" and "repeat password" are equal, if not a descriptive 
  error message is appeared.
  The password is stored as a hash value in the database in order to be more secure.
  As soon as the registration is completed the user is redirected to the login page.
