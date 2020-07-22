def my_func(*args):
    max_sum = args[0] + args[1]
    if max_sum <= args[1] + args[2]:
        max_sum = args[1] + args[2]
    if max_sum <= args[0] + args[2]:
        max_sum = args[0] + args[2]
    print(max_sum)


my_func(1, 2, 3)
