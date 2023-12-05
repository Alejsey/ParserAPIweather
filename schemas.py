from pydantic import BaseModel


class WeatherValid(BaseModel):
    name : str
    weather : int



class WeatherName(BaseModel):
    name : str
    class Config:
        orm_mode=True



class WeatherModel(BaseModel):
    name :str
    weather:int
