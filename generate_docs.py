import os
import django
import pydoc

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
django.setup()

modules = [
    "blog.models",
    "blog.views",
    "blog.admin",
    "blog.urls",
    "blog.apps",
    "blog.tests",
]

for module in modules:
    pydoc.writedoc(module)