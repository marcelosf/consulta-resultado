from django.contrib.auth.models import User


def make_user(**kwargs):
    default_user = dict(username='termen', email='termen@gil.com')
    user = dict(default_user, **kwargs)
    return user


def create_user(user_data=None):
    user = make_user()

    if user_data:
        user = dict(user, **user_data)

    user_obj = User.objects.create_user(**user)
    return user_obj
