# SAMPLE-PROJECT
#SETUP THE PROJECT

1 - create a virtual environment and activate it .then install required packages.
2 - create a django project
    django-admin startproject project_name
3 - change directory to newly created django project
4 - create an app
    django-admin startapp app_name
5 - create the application
6 - run migration commands to apply the changes to database table.
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
7 - run server
    python manage.py runserver
    
    
    
In our project a custom management command is used to populate the database with some dummy data from a json file and the user-deatil
api will return the data in the required json formmat

python manage.py newfile  -  command used to load dummy data .

