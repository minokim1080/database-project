from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'today.db'))
SQLALCHEMY_TRACK_MODIFICATION = False
SECRET_KEY= "dev"
