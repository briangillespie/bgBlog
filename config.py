import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bzumdgnndaqjnn:5v5hHBJz6kxXQAtP3mTdGKRseh@ec2-54-243-204-57.compute-1.amazonaws.com:5432/d16rap0ke7pg96'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '590517951117265',
        'secret': '492ab2453b156c347597ce618f3c9d9c'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
