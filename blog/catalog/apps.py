from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Пользователи'

    def ready(self):
        import blog.catalog.signals as signals