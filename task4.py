def my_func(x, y):
    p = x
    for count in range(abs(y) - 1):
        p *= x
    print(1 / p)


x = 10.1
y = -2
my_func(x, y)
# 0.00980296049406921
