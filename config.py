import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://bzumdgnndaqjnn:5v5hHBJz6kxXQAtP3mTdGKRseh@ec2-54-243-204-57.compute-1.amazonaws.com:5432/d16rap0ke7pg96'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'top secret!'

# OAUTH_CREDENTIALS = {
#     'facebook': {
#         'id': '590687447766982',
#         'secret': 'cd66e36c2cea3d4fff3aec3a8a174ca3'
#     },
#     'twitter': {
#         'id': 's82rsc9lTvKPWlTJDZkJyrXPv',
#         'secret': 'Z0smAsfU5QxavKO6uaMuGEyWha6lW5jLe3nKSpgbDud2rxMwb7'
#     }
#
# }

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '590517951117265',
        'secret': '492ab2453b156c347597ce618f3c9d9c'
    },
    'twitter': {
        'id': 's82rsc9lTvKPWlTJDZkJyrXPv',
        'secret': 'Z0smAsfU5QxavKO6uaMuGEyWha6lW5jLe3nKSpgbDud2rxMwb7'
    },
    'google': {
        'id': '267576082959-6is657o4tuder7m9i1f8ehlth06m4q8n.apps.googleusercontent.com',
        'secret': 'y0Ql8IIgjrjdYC6auSFpegAQ'
    }

}
