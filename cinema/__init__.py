from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cinema.config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from cinema.users.routes import users
    from cinema.posts.routes import movies
    from cinema.main.routes import main
    from cinema.errors.routes import errors

    app.register_blueprint(users)
    app.register_blueprint(movies)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

    

