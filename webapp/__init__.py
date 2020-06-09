from flask import Flask
from flask_mail import Mail
from flaskext.markdown import Markdown
from webapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
Session = sessionmaker()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session.configure(bind=engine)
session = Session()
Markdown(app)
app.static_folder = 'static'

mail = Mail(app)


from webapp import routes, models