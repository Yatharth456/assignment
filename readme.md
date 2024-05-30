# Product Inventory Management API

This is a Django-based RESTful API for managing a product inventory.

## Requirements

- Python 3.12
- Docker (optional)
- virtualenv (optional but recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Yatharth456/assignment.git
cd assignment
```

## Create a virtual environment
```bash
python -m venv venv
```

## Activate the virtual environment
on Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Create Migrations file
```bash
python manage.py makemigrations
```

## Run this command to implement migrations in your Database
```bash
python manage.py migrate
```

## Run this command to run your Django server
```bash
python manage.py runserver
```

## If you want to use the app on docker, you should have installed docker in your system, to create build for docker:
Change the `DBHOST=db` in the .env file.
```bash
docker-compose build
```

## To create container
```bash
docker-compose up
```

## To run the Test Caese run the command:
```bash
python manage.py test
```
