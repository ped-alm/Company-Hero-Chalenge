# Company-Hero-Chalenge

## Run Project
### Requirements

To run the project is necessary to have ** Python 3 ** installed on the machine along with ** pip **
It can be found at https://www.python.org/downloads/
(Remember to add Python to PATH)

### Installation

At the root of the project, the following commands must be executed in the terminal:

Creation and activation of the virtual environment (to avoid local Python pollution)

```
(Windows)
python -m venv venv 
venv\Scripts\activate.bat

(Linux)
python3 -m venv venv 
source venv/bin/activate
```

Dependencies installation

```
pip install -r requirements-dev.txt
```

### Environment configuration

Copy the ** .env_example ** file at the root of the project and create a new ** .env ** file.
Make sure that ** DEBUG ** is set ** True ** . The ** SECRET_KEY ** can be any.   

### Execution

Run the following commands

```
(Windows)
python manage.py migrate
python manage.py runserver

(Linux)
python3 manage.py migrate
python3 manage.py runserver
```
The API can be accessed at 
http://localhost:8000

### Tests

Run the following command

```
(Windows)
python manage.py test

(Linux)
python3 manage.py test
```

## Author

**Pedro Henrique de Almeida Costa**
