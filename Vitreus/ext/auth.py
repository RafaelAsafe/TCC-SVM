from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from pydaria.ext.database import db
from pydaria.models import User