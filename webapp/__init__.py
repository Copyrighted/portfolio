from flask import Flask
from flask_mail import Mail

from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


migrate = Migrate(compare_type=True)

app = Flask(__name__)
migrate.init_app(app)
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.session_protection = 'strong'
login.login_view = 'login'
migrate = Migrate(app, db)
mail = Mail(app)




from webapp import routes, models