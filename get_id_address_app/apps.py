from django.apps import AppConfig


class GetIdAddressAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'get_id_address_app'

    def ready(self):
        import get_id_address_app.signals