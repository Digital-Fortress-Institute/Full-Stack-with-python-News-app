from flask import Flask
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
 

class Base(DeclarativeBase):
    pass

apk = Flask(__name__)
db = SQLAlchemy(model_class=Base)
apk.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(apk)


class Blog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    body: Mapped[str] 
    image: Mapped[str] 

with apk.app_context():
    db.create_all()