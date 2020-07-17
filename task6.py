from pprint import pprint

continue_input = True
products = list()
index = 0

while continue_input:
    print("Input product parameters")
    name = input("Input name: ")
    cost = float(input("Input cost: "))
    count = int(input("Input count: "))
    unit = input("Input unit: ")
    index += 1
    product_dict = {"name": name, "cost": cost, "count": count, "unit": unit}
    pruduct_tuple = (index, product_dict)
    products.append(pruduct_tuple)
    check = input("Continue? (y/n): ")
    if str.lower(check) == 'y':
        ...
    elif str.lower(check) == 'n':
        continue_input = False
    else:
        print("Wrong answer. Exit")
        break

analytics = {
    "name": [],
    "cost": [],
    "count": [],
    "unit": []
}

""" For test
products = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
analytics = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}
"""

for product in products:
    for key, val in product[1].items():
        if val not in analytics[key]:
            analytics[key].append(val)

pprint(analytics)
