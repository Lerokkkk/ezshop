# EZshop

# Instalation
## 1. Cloning a repository

`git clone https://github.com/Lerokkkk/ezshop.git`

`cd ezshop`

## 2. Create virtual environment and install dependencies

`poetry install`

`poetry shell`

## 3. Rename .env_example to .env and update .env file 

## 4. Run migrations:
`cd ezshop`

`python manage.py migrate`

## 5. Create superuser
`python manage.py createsuperuser`

## 6. Run server
`python manage.py runserver`

## 7. Documentation 
[Swagger](http://127.0.0.1:8000/api/v1/schema/swagger-ui/#/)

[Login](http://127.0.0.1:8000/login/)

[Logout](http://127.0.0.1:8000/logout/)

`poetry install` - Чтобы обновить пакеты