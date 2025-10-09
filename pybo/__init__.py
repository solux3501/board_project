from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
import markdown
# from ~ import ~ : from 중에 import를 실행시키겠다
# Migrate : 데이터 구조 변경을 자동으로 관리, 변경
# SQLAlchemy : 필수는 아님. 조건 충돌 방지, DB 이식성 향상

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# DB의 이름을 자동으로 변환. ix : 인덱스 / uq : 유니크 / ck : 특정 값 조건명 / fk : 외래키명 / pk : 기본키명

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
# db라는 객체를 생성. 조건은 MetaData를 따른다
migrate = Migrate()
# Migrate 객체 생성. 지금은 생성하지 않았지만, 보통 이후에 Flask app과 DB를 연결.

def create_app():
    app = Flask(__name__)
    # Flask 앱 생성
    app.config.from_object(config)
    # config에서 설정 값 불러오기

    # ORM : SQL 간단하게 쓰는거라 생각하면 됨
    db.init_app(app)
    # SQLAlchemy 객체를 Flask앱과 연결 -> flask db migrate, flask db upgrage 명령 가능
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    # config폴더의 SQL~ 주소에 들어있는 설정 사용. 거기에 sqlite를 쓰고 있다면 true문
    # flask 객체와 db를 연결
    # render_as_batch 옵션은 컬럼 수정 / 삭제 가능 -> SQLite는 ALTER TABLE 기능(구조 변경)이 제한되어 있어 해당 기능 옵션을 써줘야함
    # sqlite 아니면 그냥 일반 방식으로 연결
    from . import models
    # 현재 패키지(.)에 models.py 불러오기
    # 위 코드 중 'db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))'는 형식만 설정하는 것임
    # 즉 ~.db 파일 내용을 여기에 연결시키겠다는 의미. 순서가 바뀌면 제대로 metadata에 전달되지 않음

    # BP
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    # 라우팅 : ~한 URL(주소)로 요청이 오면 어떤 함수를 실행할 지 설정하는 규칙
    # main_views ~ auth_view의 bp들을 Flask 앱에 등록

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    @app.template_filter("markdown")
    def markdown_filter(text):
        return markdown.markdown(
            text or "",
            extensions=['fenced_code', 'nl2br']
        )

    return app