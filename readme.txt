This is a django project made for subscription management!

** APS details **
1. http://localhost:8000/home/fetchall/ => show details about home page - carousels and description
2. http://localhost:8000/home/carousels/ => you can perform all the operations related carousels but JWT token will required!
3. http://localhost:8000/api/token/ => get JWT token on basics of correct email[username] and password
4. http://localhost:8000/account/auth/ => send the new user registration request and after successfull registration it will gets back a JWT access to user-side



** note: django admin **
email[username]: admin@admin.com
password: admin

** install required packages from requirements.txt via 'pip'
pip freeze > requirements.txt
pip install -r requirements.txt
