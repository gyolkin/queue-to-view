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

<div style="text-align: center;">
    <img style="text-align:center" src="./frontend/src/assets/qtv-small.png" alt="Project Logo">
</div>

У нас вы найдете:

:movie_camera: **Обширную базу данных**. Мы в автоматическом режиме забираем с IMDB только актуальную информацию о кинопроизведениях любых жанров. Вы точно найдете что-то по душе!

:bookmark: **Персональные списки**. Добавляйте понравившиеся фильмы в "просмотрено" или "избранное". Это поможет не обращать внимания на уже просмотренные фильмы и не забывать об отложенном на попозже.

:calendar: **Интеграцию с Google Календарем**. Запланируйте просмотр в кинотеатре или дома с помощью Google Календаря. Создать событие вы сможете прямо из интерфейса нашего сайта, а телефон сам напомнит вам о нем, когда придет время.

:loudspeaker: **Обсуждения**. Обсудите понравившуюся кинокартину в комментариях или оставьте отзыв, который поможет другим людям составить предварительное мнение о фильме.

## Запуск с помощью Docker
Клонируйте репозиторий. Создайте в корне проекта .env файл [по образцу](.env.example). Если вы не хотите, чтобы при инициализации проекта автоматически выполнился парсинг фильмов для наполнения базы данных, то установите `INCLUDE_PARSER=False`. Выполните команду:
```bash
docker compose --env-file .env up -d
```
<details>
<summary>Если контейнеры уже развернуты?</summary>

```bash
docker compose --env-file .env up --force-recreate --build -d
```
</details>

Приложение будет развернуто в трех контейнерах: db, backend, frontend, - и доступно на [localhost](http://localhost/).

## Backend
Несколько слов про бэкенд.

## Frontend
Несколько слов про фронтенд.

## Парсинг
Несколько слов про парсинг.