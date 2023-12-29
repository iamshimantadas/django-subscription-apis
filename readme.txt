This is a django project made for subscription management!

** AUTH APS details **
1. http://localhost:8000/api/login/ => get JWT token on basics of correct email[username] and password
2. http://localhost:8000/api/refresh-token/ => get refresh token of JWT
3. http://localhost:8000/account/auth/ => full CRUD of customers with JWT auth


** external apps api details **
1. http://localhost:8000/home/fetchall/ => show details about home page - carousels and description
2. http://localhost:8000/home/carousels/ => full CRUD with carousels with JWT auth
3. http://localhost:8000/api/ourteams/ => full CRUD of our teams with JWT auth
4. http://localhost:8000/api/ourteams/all/ => get all the details about our teams without AUTH - only read access
5. http://localhost:8000/api/about/ => full CRUD of about with JWT auth
6. http://localhost:8000/api/about/all/ => get about us info without JWT



** note: django admin **
email[username]: admin@admin.com
password: admin

** install required packages from requirements.txt via 'pip'
pip freeze > requirements.txt
pip install -r requirements.txt
