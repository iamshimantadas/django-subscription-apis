This is a django project made for subscription management!

** AUTH APS details **
1. http://localhost:8000/api/auth/login/ => get JWT token on basics of correct email[username] and password
2. http://localhost:8000/api/auth/refresh-token/ => get refresh token of JWT
3. http://localhost:8000/api/users/ => full CRUD of customers with JWT auth
4. http://localhost:8000/api/auth/change_password_otp => send OTP to account email for reset password
5. http://localhost:8000/api/auth/reset_password_new => submit email send's OTP and new password as well.
 

** external apps api details **
1. http://localhost:8000/home/fetchall/ => show details about home page - carousels and description
2. http://localhost:8000/home/carousels/ => full CRUD with carousels with JWT auth
3. http://localhost:8000/api/ourteams/ => full CRUD of our teams with JWT auth
4. http://localhost:8000/api/ourteams/all/ => get all the details about our teams without AUTH - only read access
5. http://localhost:8000/api/about/ => full CRUD of about with JWT auth
6. http://localhost:8000/api/about/all/ => get about us info without JWT
7. http://localhost:8000/api/chooseus/ => full CRUD of "why choose us" with JWT
8. http://localhost:8000/api/chooseus/all/ => get all info of 'why choose us' without JWT
9. http://localhost:8000/api/contact/new-request/ => send new contact request without JWT
10. http://localhost:8000/api/contact/ => full CRUD of contact forms with JWT auth
11. http://localhost:8000/api/pricing/ => full CRUD of pricing table 
12. http://localhost:8000/api/pricing/pricing-detail/ => only GET and POST method allowed for pricing 



** note: django admin **
email[username]: admin@admin.com
password: admin

** install required packages from requirements.txt via 'pip'
pip freeze > requirements.txt
pip install -r requirements.txt

test