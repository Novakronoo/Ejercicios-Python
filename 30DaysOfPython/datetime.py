# Python tiene un módulo datetime para trabajar con fechas y horas.

from datetime import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# fecha y hora actual
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Hora:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# formato mm/dd/YY H:M:S
print("Formato uno:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# formato dd/mm/YY H:M:S
print("Formato dos:", time_two)

# Convertir cadena a fecha con strptime

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# Usar date
from datetime import date

d = date(2020, 1, 1)
print(d)
print('Fecha actual:', d.today())    # fecha actual
# objeto date de hoy
today = date.today()
print("Año actual:", today.year)   # 2019
print("Mes actual:", today.month) # 12
print("Día actual:", today.day)     # 5

# Representar tiempo con objetos time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute y second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute y second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)

# Calcular la diferencia entre dos puntos en el tiempo

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Tiempo hasta año nuevo:  27 days, 0:00:00
print('Tiempo hasta año nuevo: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Tiempo hasta año nuevo:', diff) # Tiempo hasta año nuevo: 26 days, 23:01:00

# Calcular diferencias con timedelta

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)