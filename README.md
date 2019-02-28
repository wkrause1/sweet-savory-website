# Team Name
W.e.b. DuBoiz

# Members
Will Krause,
Carter Wood,
Hari Talari,
Drew Lester

# sweet-savory-website
A website being developed by Radford University students for the local business in Radford, Sweet and Savory Donuts and Bagels. 

# Requirements
- Docker and Docker-Compose

# Setup
1. `$ git clone https://github.com/wkrause1/sweet-savory-website.git`
2. `$ docker-compose up -d`
3. `$ docker-compose exec web python manage.py migrate`
4. `$ docker-compose exec web python manage.py createsuperuser`

# Accessing the sight locally
- Visit http://localhost:8000/ to view site
- Visit http://localhost:8000/admin/ and login with superuser account
   created in step 4 to add schedule data
- `$ docker-compose logs web` to see Django debug logs

# Style
This project strives to conform to [PEP8 style guidelines](http://pep8.org) in most cases.
