from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)
# M:M  테이블 정의
# ondelete='CASCADE' : 관련 내용이 삭제되면 자동으로 해당 컬럼도 삭제


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime, nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))
# id, subject, content, create_date, modify_date -> 기본 칼럼
# user_id -> 밑의 User class의 id 외래키
# user_id 와 user은 세트. 양방향으로 검색 등의 조치가 가능하도록 한 것. backref 형식은 역방향 접근이 가능하도록 옵션을 단 것
# voter 컬럼은 User 클래스와 묶어 quesdtion_voter이라는 테이블을 생성. 역방향 관계는 있고 User 클래스에 자동으로 존재하긴 하나, 이번 프로그램 상 보이진 않음

class Answer(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime, nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))
# 위와 같음

class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
# 위와 같음