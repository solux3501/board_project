from flask import Blueprint, render_template
from app.models import Post

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts = posts)