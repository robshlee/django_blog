from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): # this is necessary for using signals.py for the app
        import users.signals