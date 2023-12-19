def http_400_user_exists_details() -> str:
    return "Пользователь с такими данными уже существует"


def http_400_invalid_password_details(message: str = "причина") -> str:
    return f"Ошибка валидации пароля: {message}"


def http_400_invalid_credentials_details() -> str:
    return "Такого пользователя не существует"


def http_400_not_verified_details() -> str:
    return "Подтвердите свою учетную запись"


def http_400_already_added_to_watchlist_details() -> str:
    return "Этот фильм уже добавлен в список просмотренных"


def http_400_not_added_to_watchlist_details() -> str:
    return "Этот фильм отсутствует в списке просмотренных"


def http_404_user_not_exist_details() -> str:
    return "Данный пользователь не найден"


def http_404_country_not_exist_details(message: str | int = "default") -> str:
    return f"Страна с идентификатором {message} не найдена"


def http_404_genre_not_exist_details(message: str | int = "default") -> str:
    return f"Жанр с идентификатором {message} не найден"


def http_404_movie_not_exist_details(message: str | int = "default") -> str:
    return f"Фильм с идентификатором {message} не найден"
