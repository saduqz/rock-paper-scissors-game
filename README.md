# Rock Paper Scissors Game

The project is built using Python 3.6+, Django, Vue.js and PostgreSQL 

## Run project without install anything

1. Go to the super secure site, including https: `https://saduqz.com`


## Run locally steps

1. Clone the repository

1. Install *virtualenv* -> You can google it if you haven't installed ;)

1. Create your environment with a comment like `virtualenv venv -p python3`

1. Activate your environment with `source venv/bin/activate`

1. Install the requirements with command `pip install -r requirements.txt` into your virtual environment.

1. Create a PostgreSQL database, you will write the credentials in the next step.
 
1. Create a file in `rock_paper_scissors_game/local_info.py` (Same level than settings.py)
    - This file will contains the database and other local information
    - The content of the file should be this:
    ```
    ENGINE = "django.db.backends.postgresql"
    NAME = "your DB name"
    HOST = "localhost"
    PORT = "5432"
    USER = "your DB user"
    PASSWORD = "your DB password"
    SECRET_KEY = 'some-secure-string'
    ```
1. Run migrations with command `python manage.py migrate`

1. Run in local host: `python manage.py runserver`

1. Go to `http://localhost:8000` and enjoy it! :P

1. You can go to `http://localhost:8000/api/docs/` to see the API documentation (It's not perfect documented)


## Run Unit Test

The project has unit test for the *Rounds* API.

You can run with the command: `coverage run manage.py test`