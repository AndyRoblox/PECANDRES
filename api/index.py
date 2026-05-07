import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'historia'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'historia.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
