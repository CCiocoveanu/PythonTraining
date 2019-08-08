import datetime


class MyClass:

    def __init__(self, x=5, y="Abc"):
        self.x = x
        self.y = y

    def __str__(self):
        return "X = " + str(self.x) + " Y = " + str(self.y)

    @classmethod
    def static_stuff(cls):
        print(cls.__name__)


# p1 = MyClass(3, "D")
# print(p1.x)
# print(type(p1))
# print(p1)
MyClass.static_stuff()


class Logger:
    name = "Logger"
    location = ".\log.txt"
    writer = None

    def __init__(self, name="Logger", location="log.txt"):
        self.name = name
        self.location = location

    def __str__(self):
        return "Name = {}, Location = {}".format(self.name, self.location)

    def initiate(self):
        self.writer = open(self.location, "w")

    def close(self):
        self.writer.close()

    def log_message(self, message, level="INFO"):
        self.writer.write("{} level = {}: {}".format(datetime.datetime.now(), level, message))


log = Logger()

log.initiate()
log.log_message("Good message gets logged")
log.close()
