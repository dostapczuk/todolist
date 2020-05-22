# TodoList

## Overview
TodoList is an Django and Django Rest Framework based web app that lets the user make simple todo list with JSON. 
## Quickstart
To run app you need to install all requirements included in requirements.txt

    pip install -r requirements.txt


## Run server
To run server use this command inside manage.py directory:

    python manage.py runserver

## API
To list all todo items using API endpoint:

    /todolist/

To check single todo item using API endpoint:

    /todolist/<id>/

To create new todo item using API endpoint:
    
    POST:
    /todolist/
    
    JSON:
    {
      "title":"Title of todo item",
      "done": false/true # boolean checking if activity is completed
      "done_date": #date of finishing activity
    }
    
To delete todo item using API endpoint:

    DELETE:
    /todolist/<id>/

## Contributors
Daria Ostapczuk @dostapczuk 
