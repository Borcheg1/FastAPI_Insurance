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

6. Откройте терминал и введите команду `docker-compose up --build` и дождитесь сборки контейнеров, что может занять до 5 минут.
   В терминале вы должны увидеть сообщение `Database connection was successfull`

8. Откройте браузер и перейдите по [ссылке](http://localhost:8000/docs), далее следуйте указаниям документации API.

## Примечание
- Если на шаге 7 при переходе по ссылке у вас в терминале будут сообщения

  `Connection to database failed`

  `Error: [Errno 111] Connection refused`

  Остановите контейнеры нажатием сочетания клавиш `Ctrl+C` в терминале и повторно введите команду `docker-compose up --build`
  Данная проблема может возникнуть, если локальная машина работает медленно и контейнер с postgres не успел завершить свою инициализацию.

- По завершении работы с программой остановите контейнеры и введите команду `docker-compose down --volumes`
