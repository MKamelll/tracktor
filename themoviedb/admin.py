from django.contrib import admin
from django.contrib.admin.exceptions import AlreadyRegistered
from django.apps import apps

app = apps.get_app_config(app_label="themoviedb")

for model in app.get_models():
    try:
        admin.site.register(model_or_iterable=model)
    except AlreadyRegistered:
        pass
