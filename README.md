# Backend

This repository contains the backend code written in Python with Django. some REST endpoints.

The project directory consists of 1 main subdirectories:

* bloorprint_project = project settings directory
* library = directory containing the drivers for the different devices that can be accessed from the backend

* testapp = django application directory for the LumiPore R device

The main project directory contains:

* .venv = file with the django settings

* database.sqlite3 and MYSQL = database created after the setup instructions are performed
* manage.py = django access utility
* README.md = project README file
* requirements.txt = python dependencies file for this project

## Creating/applying migrations

After modifying/adding a database model, you must create a migration and apply it to your database.

1. Create the migration: `python3 manage.py makemigrations ` (replace app)
2. (optional) Show the migration: `python3 manage.py sqlmigrate api 0001` (replace with your migration id and app)
3. Apply the migration: `python3 manage.py migrate`
4.Start Server:`python3 manage.py runserver`

## Testing

1.Django has the possibility to run tests, to run all the unit tests, execute the following command:

```
python3 manage.py test testapp
```