import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'historia'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'historia.settings')

import django
django.setup()

os.makedirs('/tmp/staticfiles', exist_ok=True)
from django.core.management import call_command
call_command('collectstatic', '--noinput', verbosity=0)

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
