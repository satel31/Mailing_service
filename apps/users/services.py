from django.conf import settings
from django.core.mail import send_mail


def send_email(code: str, user_email: str, id) -> None:
    """Sends an email with congratulations"""
    send_mail(
        'You have almost registered!',
        f'You have almost registered on our website! Congrats!\nTo activate your account enter a code:{code}\nFollow the link: http://127.0.0.1:8000/users/{id}/activation',
        settings.EMAIL_HOST_USER,
        [user_email]
    )
