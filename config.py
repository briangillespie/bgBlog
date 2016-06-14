import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bzumdgnndaqjnn:5v5hHBJz6kxXQAtP3mTdGKRseh@ec2-54-243-204-57.compute-1.amazonaws.com:5432/d16rap0ke7pg96'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')