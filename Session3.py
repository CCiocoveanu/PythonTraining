import random
import datetime


list_setup = [7, 2, 3, 4, 5, 6, 7]
setup = list_setup[random.randint(0, len(list_setup) - 1)]

setup2 = random.choice(list_setup)
del list_setup[-1]
list_setup.sort()

print(list_setup)

s = "Python is watching"

n = s.replace("y", "j")
s.split(" ")
# print(n)

print(datetime.datetime.now())
print("Azi: {}".format(datetime.date.today()))

now = datetime.datetime.now()

print(now.date().day)  # month, year
print(now.time().hour)  # minute, second, etc.

newt = datetime.datetime(2019, 4, 30)
print("New time is ", newt)

print(newt.strftime("%Y-%m-%d, %H:%M:%S"))  # from date to string

date_string = "21 June, 2018"
print(datetime.datetime.strptime(date_string, "%d %B, %Y"))  # from string to date
