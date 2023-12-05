from pyowm.owm import OWM
from pyowm.utils.config import get_default_config


def parse_openweathermap(city):
    config_dict = get_default_config()  # Объект настройки сервиса openweathermap
    config_dict['language'] = 'ru'  # your language here, eg. Rus  Настройка языка openweathermap
    owm = OWM('916069dd302f4196c61e850ba12d9271', config_dict)  # Объявление экземпляра обьекта
    weather_mgr = owm.weather_manager()
    observation = weather_mgr.weather_at_place(city).weather
    return observation.temperature('celsius')