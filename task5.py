revenue = float(input("Выручка: "))
costs = float(input("Издержки: "))

profit = revenue - costs
profit_proc = ((revenue - costs) / costs) * 100

if profit_proc >= 0:
    print("Прибыль : {}%".format(profit_proc))
    employers_count = int(input("Введите число сотрудников: "))
    profit_per_employer = profit / employers_count
    print("Прибыль на каждого сотрудника: {}".format(profit_per_employer))
