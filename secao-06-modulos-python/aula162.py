"""
datetime(ano, mês, dia)
datetime(ano, mês, dia, horas, minutos, segundos)
datetime.strptime('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_Unix

datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html

Para timezones
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

Instalando o pytz
pip install pytz types-pytz
"""

from datetime import datetime

# from pytz import timezone


# data_str = "2022-04-20 07:49:23"
# data_format = "%Y-%m-%d %H:%M:%S"

# data01 = datetime(2022, 4, 20, 7, 49, 23)
# data02 = datetime.strptime(data_str, data_format)

# print(data01)
# print(data02)


# print(datetime.now(timezone("Asia/Tokyo")))
# print(datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone("Asia/Tokyo")))


print(datetime.now().timestamp())
print(datetime.fromtimestamp(1698957026))
