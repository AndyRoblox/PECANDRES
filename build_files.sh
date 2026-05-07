#!/bin/bash
pip install -r requirements.txt
python historia/manage.py collectstatic --noinput
