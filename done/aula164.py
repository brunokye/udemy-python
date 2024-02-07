from datetime import datetime

fmt = "%Y-%m-%d %H:%M:%S"
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime("2022-12-13 07:59:23", fmt)

print(data.strftime("%d/%m/%Y"))
print(data.strftime("%d/%m/%Y %H:%M:%S"))
