# python-flask-api
A small API using Python Programming Language and Flask Framework

## Install Python
Install Python from https://www.python.org/downloads/

## Install Flask
Run the command `pip3 install Flask`

## Database lib
`pip3 install flask_sqlalchemy`

## Run the project
To run the project, type `python app.py` on the command line

## Some Issue on development?
Problem: _Instance of 'SQLAlchemy' has no 'Column' memberpylint(no-member)_  
Solution:
	
	1. If you are using vsCode, open Command Palette
	2. Type `settings.json`
	3. Put the code below in the end of file:  
    "python.linting.pylintArgs": [
      "--load-plugins",
      "pylint-flask"
    ]

## Example of usage of CMD SQLite 
```
> python
>>> from BookModel import db
>>> db.create_all()
>>> exit()
```
