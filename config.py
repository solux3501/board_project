import os

BASE_DIR = os.path.dirname(__file__)
# BASE_DIR에 현재 파일의 절대 경로를 저장

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# ///는 절대 경로를 의미, 전체적인 맥락은 sqlite를 사용한 db 문서를 어디에 저장할 것인지 설정
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 모델 변경 추적 기능 끄기. 메모리가 증가해서 끔
SECRET_KEY = "dev"
# 세션 / 쿠기 암호화에 사용하는 키. 보통은 무작위값으로 변경해서 보호 필요하나, 개발용이라 단순 dev