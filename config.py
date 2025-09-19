import os
basedir = os.path.abspath(os.path.dirname(__file__))  # 현재 경로 -> 절대 경로로 변경한 후 저장


class Config :
 SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-me'  # key : 비밀키가 있으면 전자, 아니면 후자
 SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  'sqlite:///' + os.path.join(basedir, 'app.db')  # DATABASE 경로 : 있으면 전자, 없으면 후자
 SQLALCHEMY_TRACK_MODIFICATION = False  # 그냥 필요 없는 기능이라 생각