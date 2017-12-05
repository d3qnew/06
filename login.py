from flask.ext.login import LoginManager, login_required
from app import app

app.secret_key = 's3cr3t'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return None
