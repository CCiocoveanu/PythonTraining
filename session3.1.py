import datetime


file = open("test.txt")
content = file.read()  # citeste tot, returneaza string
cont2 = file.readline()  # citeste o linie
cont3 = file.readlines()  # citeste si ret o lista cu toate liniile
print(file.read())
file.close()

with open("test.txt") as file:
    for line in file.readlines():
        print(line)

with open("results.txt", "a")as writer:
    writer.write("Prima linie\n")
    writer.write("2 linie")
