from sqlalchemy import update
from sqlalchemy.orm import Session
import models


async def get_weather_for_name(db: Session, name:str):
    return db.query(
        models.Weather.weather
    ).filter(models.Weather.name == name).first()


async def get_weather_all(db:Session):
    return db.query(models.Weather).all()

async def only_create_name_city(db:Session , data: str):
    db.add(data)
    db.commit()
    db.refresh(data)
    return db



def get_name_ex(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weather.name).offset(skip).limit(limit).all()


def getWeather_city(city: str, conn : Session):
    return conn.query(models.Weather).filter(models.Weather.name==city).first()



def back(db: Session):
    name = db.query(models.Weather.name).all()
    print(type(name))

def _update(city, weather):
    stmt = (
        update(models.Weather).
        where(models.Weather.name == city).
        values(weather=weather)
    )
    return stmt



def get_user_by_email(db: Session):
    return db.query(models.Weather).filter().first()


"""from sqlalchemy.orm import Session

from . import  models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_use r


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item"""


