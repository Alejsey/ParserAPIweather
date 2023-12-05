
import pandas
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config() # Объект настройки сервиса openweathermap
config_dict['language'] = 'ru'  # your language here, eg. Rus  Настройка языка openweathermap
owm = OWM('916069dd302f4196c61e850ba12d9271', config_dict)# Объявление экземпляра обьекта
weather_mgr = owm.weather_manager()
observation = weather_mgr.weather_at_place('London')
APIkey =  '74810782b332bd94dc99a9bff519259a'
# Список всех городов
cities  = pandas.read_excel('cities_list.xlsx')
ls_cities = cities.name # class 'pandas.core.series.Series
""" 
observation = weather_mgr.weather_at_place('London')
observation.weather
<pyowm.weatherapi25.weather.Weather - reference_time=2023-10-19 12:52:50+00:00, status=rain, detailed_status=небольшой дождь>
"""
