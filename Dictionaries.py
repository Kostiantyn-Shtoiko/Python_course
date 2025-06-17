car_prices = {'bmw' : 5000, 'opel' : 2000, 'toyota' : 10000}
print(car_prices['opel'])
car_prices['mazda'] = 4000
print(car_prices['mazda'])
print(car_prices)

del car_prices['opel']
print(car_prices)

car_prices.clear()
print(car_prices)

person = {
    'first name' : 'Kosta',
    'last name' : 'Shtoiko',
    'age' : 19,
    'hobbies' : 'IT',
    'car' : ['bmw', 'opel', 'toyota']
}
print(person['age'])
print(person['car'] [1])
print(person)

person['car'][0] = 'VW'
print(person['car'])

# Homework

person = {
    "name": "Alice",
    "age": 30,
    "city": "Kyiv"
}

print(person["name"])

computer = {
    "brand": "Dell",
    "model": "XPS 15",
    "processor": {
        "brand": "Intel",
        "model": "Core i7-12700H",
        "cores": 14,
        "threads": 20
    },
    "ram": {
        "size_gb": 32,
        "type": "DDR5"
    },
    "storage": [
        {"type": "SSD", "capacity_gb": 1000},
        {"type": "HDD", "capacity_gb": 2000}
    ],
    "gpu": {
        "brand": "NVIDIA",
        "model": "RTX 4060",
        "memory_gb": 8
    },
    "os": "Windows 11 Pro",
    "year": 2023,
    "ports": ["USB-C", "HDMI", "Thunderbolt 4", "3.5mm audio"],
    "wifi": True,
    "bluetooth": True
}