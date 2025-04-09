import json
import os
from django.conf import settings


def load_data():
    file_path = os.path.join(settings.BASE_DIR, 'main', 'data', 'data.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    return content