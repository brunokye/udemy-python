from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y %H:%M:%S"
data_inicio = datetime.strptime("20/04/1987 09:30:30", fmt)
data_fim = datetime.strptime("12/12/2022 08:20:20", fmt)
delta = timedelta(days=45)

print(data_inicio)
print(data_fim)

print(f"\n{20 * '-'}\n")

print(data_fim - delta)
print(data_inicio - data_fim)

print(f"\n{20 * '-'}\n")

print(relativedelta(data_fim, data_inicio))
