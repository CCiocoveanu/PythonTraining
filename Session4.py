str_list = [1, 2, 5, 8, 12, 78, 234658, -12, 0]

for content in str_list:
    # print(content)
    pass

for i in range(0, -1):
    # print(str_list[i])
    pass

i = 0
while i < len(str_list):
    # print(str_list[i])
    i = i + 1

try:
    #  print(3)
    pass
except NameError as err:
    print("Something bad")
    print(str(err.args))
except (TabError, EnvironmentError):
    print("Tab error")
else:
    #  print("No problem")
    pass
finally:
    #  print("Executed all the time")
    pass

dict_ex = {
    "unu": "1",
    "doi": "2",
    "trei": "3",
    "patru": "3"
}

# print(dict_ex.get("un", "Nu am gasit"))  # in caz ca nu gaseste nimic

for elem in dict_ex:
    # print(dict_ex.get(elem))
    pass

for elem in dict_ex.values():
    # print(elem)
    pass

for key, value in dict_ex.items():
    print(key, "is", value)

if "unu" in dict_ex:
    print(dict_ex.get("unu"))
else:
    print("Nu e unu")

# dict 10 cuv > 15 > 12
