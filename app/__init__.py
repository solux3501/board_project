# Flask의 팩토리 함수 패턴이라 함.

from flask import Flask  # 웹 프레임 워크
from config import Config  # 환경변수, key 담당
from flask_sqlalchemy import SQLAlchemy  # ORM(DB관리) : 객체-관계 매핑. sql 안쓰는 방법임
from flask_migrate import Migrate  # DB 마이그레이션 도구(테이블 구조 변경 자동화)
from flask_login import LoginManager  # 사용자 로그인 / 세션 관리

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'

def create_app(config_class = Config) :  # create_app : Flask 앱을 생성하는 팩토리 함수
    app = Flask(__name__, template_folder = 'templates', static_folder = 'static') # 템플릿 / 정적 파일 경로 설정
    app.config.from_object(config_class)  # config 클래스에서 설정 불러오기

    db.init_app(app)  # flask와 SQL 연결
    migrate.init_app(app, db)  # flask와 마이그레이션 연결
    login.init_app(app)  # flask와 로그인 관리자 연결

    from app.route import bp as main_bp  # app.route 모듈에서 bp라는 객체를 가져와 main_bp라 칭함
    app.register_blueprint(main_bp)  # flask 앱에 라우트 등록. 앱에서 URL 주소와 지금 내가 만든 함수를 연결하는 것을 칭함

    return app