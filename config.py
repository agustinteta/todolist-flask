import os

SECRET_KEY = 'secret_key',
DATABASE_HOST = os.environ.get('FLASK_DATABASE_HOST'),
DATABASE_PASSWORD = os.environ.get('FLASK_DATABASE_PASSWORD'),
DATABASE_USER = os.environ.get('FLASK_DATABASE_USER'),
DATABASE = os.environ.get('FLASK_DATABASE'),
    