from django.apps import AppConfig

from webapp import products


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp.products'
