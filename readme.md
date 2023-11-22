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

## Major Commits
<details>
<summary>feature/auth</summary>
Реализована система аутентификации и авторизации пользователей. Клиент отправляет данные > сервер проверяет существование такого пользователя > генерирует и устанавливает в браузер пользователя JWT-токен в httpOnly куке. На фронтэнде создается еще одна кука с таким же сроком жизни (7 дней) — она служит в качестве маркера, что пользователь был авторизован.

**[backend]** На стороне бэкенда в основу системы легла библиотека [FastAPI Users](https://github.com/fastapi-users/fastapi-users). Некоторые вещи были изменены. Например:
1. Роут */auth/login* в нашей реализации принимает запросы в кодировке ```application/json```, как и все остальные роуты, а не в кодировке ```application/x-www-form-urlencoded```, как это сделано по умолчанию [[issue]](https://github.com/fastapi-users/fastapi-users/issues/358).
2. Роут */auth/login* принимает связку данных в формате ```email:password```, как и */auth/register*. Это логичный подход, тем не менее в реализации по умолчанию роут */auth/login* принимает связку данных в формате ```username:password``` [[issue]](https://github.com/fastapi-users/fastapi-users/issues/273).
3. Исправлена неконсистентность ответов, которая присуща библиотеке. Например, ответ об ошибке может вернуться как в виде строки, так и в виде объекта [[issue]](https://github.com/fastapi-users/fastapi-users/issues/1318):
```json
{
    "detail": "Привет! Я нормальный ответ."
}
```
```json
{
    "detail": {
        "code": "WTF?",
        "reason": "А вот я не очень... хотя это как посмотреть."
    }
}
```
Наше API плюется ошибками в строго определенном формате (первом).

**[frontend]** На фронтэнде реализованы формы регистрации и авторизации пользователей, сделан задел на профиль, добавлен компонент-защитник приватных роутов. Добавлена валидация данных на фронте, например, пустая форма не уйдет на сервер. 
</details>