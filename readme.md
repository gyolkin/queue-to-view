# Проект: Queue to View
<a href="https://fastapi.tiangolo.com/" target="_blank">
    <img src="https://img.shields.io/badge/fastapi-009485?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
</a>
<a href="https://react.dev/" target="_blank">
    <img src="https://img.shields.io/badge/react-087ea4?style=for-the-badge&logo=react&logoColor=white" alt="React">
</a>
<a href="https://www.docker.com/" target="_blank">
    <img src="https://img.shields.io/badge/docker-1d63ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</a>

## Описание проекта
**Queue to View** — это не просто еще один веб-каталог с фильмами. Это место, где кинолюбители любых интересов смогут планировать походы в кинотеатры или просмотр фильмов дома, общаться с единомышленниками и всегда найти ответ на вопрос: а что сегодня посмотреть?

<p align="center">
    <img style="text-align:center" src="./frontend/src/assets/qtv-small.png" alt="Project Logo">
</p>

У нас вы найдете:

:movie_camera: **Обширную базу данных**. Мы в автоматическом режиме забираем с IMDB только актуальную информацию о кинопроизведениях любых жанров. Вы точно найдете что-то по душе!

:bookmark: **Персональные списки**. Добавляйте понравившиеся фильмы в "просмотрено" или "избранное". Это поможет не обращать внимания на уже просмотренные фильмы и не забывать об отложенном на попозже.

:loudspeaker: **Обсуждения**. Обсудите понравившуюся кинокартину в комментариях или оставьте отзыв, который поможет другим людям составить предварительное мнение о фильме.

## Запуск с помощью Docker
Клонируйте репозиторий. Создайте в корне проекта .env файл [по образцу](.env.example). Выполните команду:
```bash
docker compose --env-file .env up -d
```
<details>
<summary>Если контейнеры уже развернуты?</summary>

```bash
docker compose --env-file .env up --force-recreate --build -d
```
</details>

Приложение будет развернуто в трех контейнерах: db, backend, frontend, - и доступно по адресу [127.0.0.1](http://127.0.0.1/). Интерактивная API-документация по умолчанию доступна по адресу [127.0.0.1/docs](http://127.0.0.1/docs). Этот адрес при желании можно изменить, указав соответствующее значение переменной окружения ```DOCS_URL```.

### Первоначальная настройка приложения
Поскольку вы самостоятельно запускаете приложение на своей локальной машине, база данных не будет содержать каких-либо записей. Для быстрого заполнения базы данных пользователями и фильмами (из JSON файла) предусмотрены консольные команды. Выполните следующие шаги:

```bash
docker exec -it backend bash
```

Теперь вы сможете выполнять команды напрямую из backend-контейнера. Первым делом необходимо создать суперпользователя. Учтите, что ```qtv``` — по сути алиас для ```python -m cli```, чтобы команды можно было выполнять быстрее и удобнее.

```bash
qtv createuser
```

Далее в интерактивном режиме вам будет необходимо ввести Email, пароль, указать права (администратор или обычный пользователь). Чтобы быстро заполнить базу данных жанрами и фильмами, выполните:

```bash
qtv movieimport -f movies.json
```

В интерактивном режиме авторизуйтесь, указав данные суперпользователя, которого только что создали. Это необходимо, поскольку команда использует защищенный API-эндпоинт для создания записей о фильмах. Она дополнительно создает все необходимые жанры, если жанров в базе данных еще нет. 

## Backend
Несколько слов про бэкенд.

## Frontend
Несколько слов про фронтенд.

## Парсинг
Несколько слов про парсинг.
