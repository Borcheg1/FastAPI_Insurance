# Check FastAPI insurance rate
![Static Badge](https://img.shields.io/badge/Python-3.11-blue)
![Static Badge](https://img.shields.io/badge/FastAPI-red)
![Static Badge](https://img.shields.io/badge/Database-PostgreSQL-ygreen)
![Static Badge](https://img.shields.io/badge/ORM-Tortoise-orange)

### Тестовое задание на знание FastAPI

## Руководство по установке и запуску приложения

1. Откройте терминал и введите команду
`git clone https://github.com/Borcheg1/FastAPI_Insurance.git`

2. Перейдите в рабочую дерикторию проекта:
`cd FastAPI_Insurance/`

3. Переименуйте файл `env_example` в `.env` в корневой папке проекта и введите свой пароль для переменной `DB_PASS=your_password`

4. Откройте файл `docker-compose.yml` в корневой папке проекта и введите свой пароль в переменной `POSTGRES_PASSWORD=your_password`

5. Запустите приложение `Docker Desktop`

6. Откройте терминал и введите команду `docker-compose up --build` и дождитесь сборки контейнеров 

7. Откройте браузер и перейдите по [ссылке](http://localhost:8000/docs), далее следуйте указаниям документации API.
