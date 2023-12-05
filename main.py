"""

"""
import time
from fastapi import FastAPI, Depends, Path, Query, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi_utils.tasks import repeat_every

from typing import Annotated
import json


from sqlalchemy.orm import Session

from crud import _update, getWeather_city, get_name_ex
from database import SessionLocal, engine
from models import Weather, Base

from schemas import WeatherValid, WeatherName
from parserEngine import parse_openweathermap


app = FastAPI(title="openAPIparser",
              description="Коллектор который собирает данные при запросе и обновляет их каждый час",
              )


Base.metadata.create_all(bind=engine)


### 1 Реализован парсер названий городов они нужны для аргумента парсера openweathermap а так же можно реализовать механинку?  добаление из этих данных в список выбранных городов
### Эту механику можно реализовать для юсера или неавторизванного юзера?: как?
### 2 Реализован парсер погоды с openweathermap
### 3 спроектированна база данных
### 4 доделать соединени к бд
### Подумать о асихрнке
### Подумать о очереди задач и о брокере

"""@app.on_event("startup")
def copy():
    for city in ls_cities:
        stmt = insert(Weather).values(name=city)
        with engine.connect() as conn:
            result = conn.execute(stmt)"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get('/', response_model=list[WeatherName])
async def get_name(response: Response,
                   db: Session = Depends(get_db),
                   q:Annotated[int, Query(description = "Начать с такого то номера ")] = None):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return get_name_ex(db, q)


@app.get('/Weather_for_city')
async def get_weather(response: Response, city: str, db: Session = Depends(get_db)):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {
        "city" : city,
        "weather" : (getWeather_city(city, db))
    }

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <label>Item ID: <input type="text" id="itemId" autocomplete="off" value="foo"/></label>
            <label>Token: <input type="text" id="token" autocomplete="off" value="some-key-token"/></label>
            <button onclick="connect(event)">Connect</button>
            <hr>
            <label>Message: <input type="text" id="messageText" autocomplete="off"/></label>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
        var ws = null;
            function connect(event) {
                var itemId = document.getElementById("itemId")
                var token = document.getElementById("token")
                ws = new WebSocket("ws://localhost:8000/items/" + itemId.value + "/ws?token=" + token.value);
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                event.preventDefault()
            }
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""



"""@app.get('/parser')
async def get():
    return render_component('src/index.js')
"""



@app.on_event("startup")
@repeat_every(seconds=60)
async def parse_weather(connection : Session = next(get_db())):
    """ Функция которая обновляет каждую минуту погоду"""
    start = time.time()

    count = 0
    try :
        for city in connection.query(Weather.name).all():
            weather = parse_openweathermap(city[0])['temp']  #{'temp': 17.58, 'temp_max': 19.04, 'temp_min': 15.83, 'feels_like': 16.73, 'temp_kf': None}
            connection.execute(_update(city[0], weather))
            count +=1

    except:
        print(f'error from {count}')

    stop = time.time()
    print(stop-start)




"""conn.execute(select(Weather.name).where(Weather.name == city).order_by(Weather.name))
conn.execute(update(Weather).values(weather=weather))
conn.close()"""
