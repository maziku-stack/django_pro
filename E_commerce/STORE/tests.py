from django.test import TestCase
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')  # <-- This is where Solution #1 goes
django.setup()

from TAGS.models import MyModel
from STORE.models import MyModel
print(MyModel.objects.all())