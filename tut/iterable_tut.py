import math
from pprint import pprint as pp

words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
comprehension = [len(word) for word in words]
print(comprehension)

country_to_capital = {
    "UK": "London",
    "Brazil": "Brazilia",
    "Morocco": "Rabat",
    "Sweden": "Stockholm"
}
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)


def get_factorial_digits():
    return [len(str(math.factorial(x))) for x in range(20)]


if __name__ == "__main__":
    print(get_factorial_digits())

