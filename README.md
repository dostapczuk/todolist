# TodoList

## Overview
TodoList is a Django and Django Rest Framework based web app that lets the user make simple todo list with JSON. 
## Quickstart
### Pre-requirements
Make sure you have Python 3.x installed as well as pip.
### Requirements
To run app you need to install all requirements included in requirements.txt

    pip install -r requirements.txt


### Run server
To run server use this command inside manage.py directory:

    python manage.py runserver

## API
To list all todo items using API endpoint:

    /todolist/
    
    Response:
    [
    {
        "id": 2,
        "title": "",
        "done": false,
        "author_ip": "",
        "created_date": "2020-05-22T18:30:02.902418Z",
        "done_date": null
    },
    {
        "id": 3,
        "title": "",
        "done": false,
        "author_ip": "",
        "created_date": "2020-05-22T18:37:04.664953Z",
        "done_date": null
    },
    ]
    status 200 OK

To check single todo item using API endpoint:

    /todolist/<id>/
    
    Response:
    {
        "id": 2,
        "title": "",
        "done": false,
        "author_ip": "",
        "created_date": "2020-05-22T18:30:02.902418Z",
        "done_date": null   
    } 
    status: 200 OK

To create new todo item using API endpoint:
    
    POST:
    /todolist/
    
    JSON:
    {
      "title":"Title of todo item",
      "done": false/true # boolean checking if activity is completed
      "done_date": # date of finished activity
    }
    
    Example:
    
    Request JSON:
    {
	    "title": "Title of todo item",
	    "done": false
    }
    
    Response:
    {
        "id": 13,
        "title": "Title of todo item",
        "done": false,
        "author_ip": "127.0.0.1",
        "created_date": "2020-05-23T13:12:14.666081Z",
        "done_date": null
    }
    status: 201 Created
    
To delete todo item using API endpoint:

    DELETE:
    /todolist/<id>/
    
    Response:
    {}
    status: 204 No Content

## Contributors
Daria Ostapczuk @dostapczuk 
