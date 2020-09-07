# Company-Hero-Chalenge

Challenge done as a step in the Company Hero selection process. The project was created using the frameworks
**Django** and **Django Rest Framework** on **Python 3**

The published application can be accessed through Heroku at https://company-hero-challenge.herokuapp.com/

## Proposed Solution

Following the challenge requirements I have created 3 models.

Person -> An enriched wrapper for the Django.User representing the platform users.  
Company -> A model representing the company.  
Employee -> The representation of the many-to-many relationship between the Person and Company.

The Person and Company have the full CRUD implemented. The Employee was limited to not be updatable to simplify implementation.
The Employee.job was not normalized for the same motives.

The route to access all the company data is http:<host>/companies/<company_id>/full_company/  
The route to access all the person data is http:<host>/persons/<person_id>/full_person/  

I used the person id to access the second route instead of the username because I thought it would be more semantic.

## Some Problems

Due to time restriction I couldn't configure the CI/CD proccess and some tests were skipped.

## Run Project
### Requirements

To run the project is necessary to have **Python 3** installed on the machine along with **pip**
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

Copy the **.env_example** file at the root of the project and create a new **.env** file.
Make sure that **DEBUG** is set **True** . The **SECRET_KEY** can be any.   

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
