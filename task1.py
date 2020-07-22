def division(*args):
    try:
        return args[0] / args[1]
    except ZeroDivisionError:
        print("ERROR divider is equals to 0")
        return None


dividend = float(input("Input dividend: "))
divider = float(input("Input divider: "))

print(division(dividend, divider))
