import os

class config (object):
    USER = os.environ.get('POSTGRES_USER', '-')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '-')
    HOST = os.environ.get('POSTGRES_HOST', '-')
    PORT = os.environ.get('POSTGRES_PORT', '-')
    DB = os.environ.get('POSTGRES_DB','-')

    SQLCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = '77evgiqjbv7;a;vkbha__-_vmb;HIB'
    SQLCHEMY_TRACK_MODIFICATIONS = True
 
