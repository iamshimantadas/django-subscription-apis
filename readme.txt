carousel:http://localhost:8000/api/carousel/
users CRUD: http://localhost:8000/api/users/
contact us: http://localhost:8000/api/contact-us/
all plans: http://localhost:8000/api/subscription/plans/
buy plan: http://localhost:8000/api/subscription/buy/
active plan: http://localhost:8000/api/subscription/active-plan/cus_PNtnajw7FhA2Ju/

------------------------------------------------------
basic login credentials
{
  "email": "admin@admin.com",
  "password": "admin"
}
{
  "email": "anirban@mail.com",
  "password": "anirban@mail.com"
}
-----------------------------------------------------------
for maing payment 4 parameters required:
{
"product_obj":"prod_PMRNQ5K4X0tc4O",
"price_obj":"price_1OXiUySGnyUJDQBRqxzf0GYv",
"quantity":"1",
"custid":"cus_PNtnajw7FhA2Ju"
}
** Note: this 'custid' you will get during registration and login both.
---------------------------------------------------------------
Note: pass customerid for active plan api route.