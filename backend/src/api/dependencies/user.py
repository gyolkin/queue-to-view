from src.config.authentication import authenticator
from src.config.manager import settings

current_user = authenticator.current_user(
    active=True, verified=settings.REGISTER_VERIFICATION
)
current_user_optional = authenticator.current_user(
    active=True, verified=settings.REGISTER_VERIFICATION, optional=True
)
current_superuser = authenticator.current_user(active=True, superuser=True)

current_user_token = authenticator.current_user_token(
    active=True, verified=settings.REGISTER_VERIFICATION
)
