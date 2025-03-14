import os

class config (object):
    USER = os.environ.get('POSTGRES_USER', 'skimmer')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'skimerUNIX')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', '5427')
    DB = os.environ.get('POSTGRES_DB','db_cite')

    SQLCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = '77evgiqjbv7;a;vkbha__-_vmb;HIB'
    SQLCHEMY_TRACK_MODIFICATIONS = True
 