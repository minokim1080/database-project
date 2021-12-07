from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'today.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'k\x9e&\xc7\xde"\xea/\x0bX[:\xda\x89\xdf\xa0'
