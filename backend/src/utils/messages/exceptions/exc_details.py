def http_400_user_exists_details() -> str:
    return "Пользователь с такими данными уже существует"


def http_400_invalid_password_details(message: str) -> str:
    return f"Некорректный пароль: {message}"


def http_400_invalid_credentials_details() -> str:
    return "Такого пользователя не существует"


def http_400_not_verified_details() -> str:
    return "Подтвердите свою учетную запись"


def http_404_user_not_exists_details() -> str:
    return "Данный пользователь не найден"
