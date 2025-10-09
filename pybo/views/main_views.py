from flask import Blueprint, url_for
from werkzeug.utils import redirect
# WSGI(Web Server GateWay Interface) : 웹서버 <-> WSGI <-> python 연결해주는 표준 인터페이스
# werkzeug : 도구라는 뜻의 독일어
# from flask import redirect 도 있는데 별 차이는 없음(오히려 werkzeug가 더 구식). 다음부턴 그냥 해당 모듈로 import시키자.
# redirect : 클라이언트를 다른 URL로 이동시키는 기능

bp = Blueprint('main', __name__, url_prefix='/')
# 현재 파일의 이름(name)으로 bp 이름은 main. 뒤에 '/'가 붙은 것들을 말함

@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'
# '~/hello'로 접속하면 해당 파일이 실행 -> 결과는 return

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
# '~/'로 접속하면 'question' bp의 _list() 함수를 찾아 반환