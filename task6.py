a = float(input("a: "))
b = float(input("b: "))

day_num = 1
day_dist = a

while day_dist <= b:
    day_dist *= 1.1
    day_num += 1

print(day_num)
