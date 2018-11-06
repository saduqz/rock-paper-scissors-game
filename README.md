# Rock Paper Scissors Game

The project is built using Python 3.6+, Django, Vue.js and PostgreSQL 

## Run project without install anything

0. Go to the super secure site, including https: `https://saduqz.com`


## Run locally steps

0. Clone the repository

0. Install *virtualenv* -> You can google it if you haven't installed ;)

0. Create your environment with a comment like `virtualenv venv -p python3`

0. Activate your environment with `source venv/bin/activate`

0. Install the requirements with command `pip install -r requirements.txt` into your virtual environment.

0. Create a PostgreSQL database, you will write the credentials in the next step.
 
0. Create a file in `rock_paper_scissors_game/local_info.py` (Same level than settings.py)
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
0. Run migrations with command `python manage.py migrate`

0. Run in local host: `python manage.py runserver`

0. Go to `http://localhost:8000` and enjoy it! :P


## Run Unit Test

The project has unit test for the *Rounds* API.

You can run with the command: `coverage run manage.py test`