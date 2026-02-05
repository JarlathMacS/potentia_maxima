# Potentia | Maxima

# Deployment

- The app is deployed to [Heroku](https://heroku.com)
- The database is [PostgreSQL](https://www.postgresql.org) hosted by [Code Institute](https://dbs.ci-dbs.net/manage)
- The app can be accessed by this [link](https://potentia-7a9209d492dd.herokuapp.com)

## Local Deployment

*Note:*
  - This project requires to install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`


1. Clone the repository.

    - ```git clone https://github.com/JarlathMacS/potentia_maxima.git```

2. Go to the ```potentia_maxima``` directory.

    - ```cd potentia_maxima```

3. Create a virtual environment.

    - ```python3 -m venv venv```

    - ```source venv/bin/activate```

4. Install all dependencies.

    - ```pip3 install -r requirements.txt```

5. Create a ```env.py``` file.

    - ```touch env.py```

6. Add the following lines to ```env.py```:

    - ```import os```
    - ```os.environ["SECRET_KEY"]``` = your secret key.
    - ```os.environ["DEBUG_VALUE"]``` = "True" or "False" depending on whether you are in development or production.
    - ```os.environ["DATABASE_URL"]``` = your database url.
    - ```os.environ["CLOUDINARY_URL"]``` = your cloudinary url.

7. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

8. Create and migrate the database:

    1. Run the following commands in a terminal to make migrations: 
        - `python3 manage.py makemigrations`
        - `python3 manage.py migrate`
    1. Create a superuser to get access to the admin environment.
        - `python3 manage.py createsuperuser`
        - Enter the required information (your username and password).
    1. Run the app with the following command in the terminal:
        - `python3 manage.py runserver`
    1. Open the link provided in a browser to see the app.

    1. If you need to access the admin page:
        - Add /admin/ to the link provided.
        - Enter your username and password (for the superuser that you have created before).
        - You will be redirected to the admin page.

---
## Heroku Deployment


1. Create a Heroku account if you don't already have one.

2. Create a new app on Heroku.

    1. Go to the [Heroku dashboard](https://dashboard.heroku.com/apps).
    2. Click on the "New" button.
    3. Click on the "Create new app" button.
    4. Choose a name for your app.
    5. Choose a region.
    6. Click on the "Create app" button.

3. In your app go to the "Resources" tab.

    1. Add a Heroku Postgres database.

4. In your app, go to the "Settings" tab, press "Reveal Config Vars", and add the following config vars if they are not already set:

    1. ```DEBUG``` = True during development, False during production.
    2. ```DATABASE_URL``` = the url of your postgres database.
    3. ```SECRET_KEY``` = a secret key for your app.
    4. ```CLOUDINARY_URL``` = your cloudinary url.
    5. ```DISABLE_COLLECTSTATIC``` = 1 during development. Remove this when deploying to production.

5. In your app go to the "Deploy" tab.

    1. If it's already possible, connect your Heroku account to your GitHub account and then click on the "Deploy" button.
    2. If not, you need to copy the Heroku CLI command to connect your heroku app and your local repository.

        - ```heroku git:remote -a <your-heroku-app-name>```

6. Go to your local repository.

7. Login to your Heroku account in your terminal and connect your local repository to your heroku app.

    1. ```heroku login -i``` - Enter all your Heroku credentials it will ask for.
    2. Paste the command you copied from step 5 into your terminal.

8. Create Procfile in your local workplace.

    This file will will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.

9. Create ```requirements.txt```. This can be done by running the following command:

    - ```pip3 freeze > requirements.txt```

10. Add and commit all changes.

11. Push your changes to Heroku.

    - ```git push```

12. Check your app's logs in heroku dashboard and ensure everything is working.

13. After the development is done, you can change the ```DEBUG``` config var to ```False``` and remove the ```DISABLE_COLLECTSTATIC``` config var from the config vars on heroku.


---
---



[Back to top](#potentia--maxima)

---

