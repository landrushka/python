input_month = int(input("Input month: "))

if not (1 <= input_month <= 12):
    print("Wrong input")
    exit(1)

months_dict = {1: "January",
               2: "February",
               3: "March",
               4: "April",
               5: "May",
               6: "June",
               7: "July",
               8: "August",
               9: "September",
               10: "October",
               11: "November",
               12: "December"}

print(months_dict[input_month])

months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

print(months_list[input_month - 1])
