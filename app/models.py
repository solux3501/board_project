from datetime import datetime  # 시간 관련
from app import db, login  # ??
from flask_login import UserMixin  # flask_login이 요구하는 속성, 메서드 사용
from werkzeug.security import generate_password_hash, check_password_hash  # 비밀번호 관련

class User(UserMixin, db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'author', lazy = 'dynamic')

    def set_password(self, password) :  # 해시 비밀번호 생성
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) :  # 해시 비밀번호 검증
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(user_id) :
    return Usser.query.get(int(user_id))

class Post(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140), nullable = False)
    content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeginKey('user.id'))
    comments = db.relationship('Comment', backref = 'post', lazy = 'dynamic')

class Comment(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text,nullable = False)
    created_At = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeginKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeginKey('post.id'))
    # learn_plask. 0918