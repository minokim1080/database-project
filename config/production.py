from config.default import *

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user='dbmasteruser',
        pw='Q4%*4p5KNxZj9S&O?LQk((VgH5`IkjU9'
        url=' ls-73647d1b23a063a11b30fbbb4a0fb48995082594.ce6ming3ugdm.ap-northeast-2.rds.amazonaws.com',
        db='flask_today')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'k\x9e&\xc7\xde"\xea/\x0bX[:\xda\x89\xdf\xa0'
