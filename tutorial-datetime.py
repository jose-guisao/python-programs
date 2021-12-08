import datetime
import pytz # to work woth timezone
'''
Directive	Meaning
%a			Weekday as locale’s abbreviated name.
%A			Weekday as locale’s full name.
%w			Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d			Day of the month as a zero-padded decimal number.
%b			Month as locale’s abbreviated name.
%B			Month as locale’s full name.
%m			Month as a zero-padded decimal number.
%y			Year without century as a zero-padded decimal number.
%Y			Year with century as a decimal number.
%H			Hour (24-hour clock) as a zero-padded decimal number.
%I			Hour (12-hour clock) as a zero-padded decimal number.
%p			Locale’s equivalent of either AM or PM.
%M			Minute as a zero-padded decimal number.
%S			Second as a zero-padded decimal number.
%f			Microsecond as a decimal number, zero-padded on the left.
%z			UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).
%Z			Time zone name (empty string if the object is naive).
%j			Day of the year as a zero-padded decimal number.
%U			Week number of the year (Sunday as the first day of the week) as a zero padded 
			decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.
%W			Week number of the year (Monday as the first day of the week) as a decimal number. 
			All days in a new year preceding the first Monday are considered to be in week 0.
%c			Locale’s appropriate date and time representation.
%x			Locale’s appropriate date representation.
%X			Locale’s appropriate time representation.
%%			A literal '%' character.
'''
#Return string in ISO 8601 format, YYYY-MM-DD.
print("Formato de fecha")
print()
jdg = datetime.date(1962,8,15) # Date of my birthday

print("The date of my birthday was", jdg.strftime("%A , %B %d, %Y"))
message = "JDG was born on {:%A, %B %d, %Y}."
print(message.format(jdg))
print("Año ", jdg.year)
print("Mes ", jdg.month)
print("Día ", jdg.day)

millenium = datetime.date(2000, 1, 1)
print("Fecha del milenio ", millenium,)
# 200 days after the millenium 
# Using timedelta method
dt = datetime.timedelta(200)
print("200 días despues del milenio ", millenium + dt)
print()
print("SPACEX")
print("Reused first stage rocket: March 30, 2017 22:27 UTC")
print()
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print("Date included YYYY-MM-DD  ", launch_date)
print("Time only HH:MM:SS", launch_time)

#YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS

print("Datetime includes YYYY-MM-DD HH:MM:SS", launch_datetime)
print("HH", launch_time.hour)
print("MM", launch_time.minute)
print("SS", launch_time.second)
print("Method launch_datetime")
print("YYYY", launch_datetime.year)
print("MM", launch_datetime.month)
print("DD", launch_datetime.day)
print("HH", launch_datetime.hour)
print("MM", launch_datetime.minute)
print("SS", launch_datetime.second)
print()
print("Today method datetime.datetime.today() includes microseconds")
now = datetime.datetime.today()
print("Today date is:", now)
print("microseconds", now.microsecond)
print()
print("Convert string to datetime:")
print("Moon landing '7/20/1969'")
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print("UTC date/time", dt_utcnow)
dt_pr = dt_utcnow.astimezone(pytz.timezone('America/Puerto_Rico'))
print("PR  date/time", dt_pr)
print()
# Reference video https://www.youtube.com/watch?v=eirjjyP2qcQ  mins 15:00
# Using timezone module pytz
print("List of all time in pytz module")
for tz in pytz.all_timezones:
    if "Puerto" in tz:
        print(tz)
#
# Ejercicio
#Abraham Lincoln was born on February 12th two hundred and eleven years ago 211
# Actual date of born February 12, 1809
#Calcular el año usando el timedelta method, hint convertir dias a años
# Expresarlo en el dia de la semana
al_bday = "February 12, 1809"
print("Abraham Lincoln - February 12, 1809")
al = datetime.datetime.strptime(al_bday, "%B %d, %Y")
al_today = (now - al).days/365
print(al_today,"years")
# al_dbay_in_days = 365 * 211
# dt = datetime.timedelta(al_dbay_in_days)        
# print(now)
# print(dt)
# al_today = now - dt
# print(al_bday.strftime("%A , %B %d, %Y"))