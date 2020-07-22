continue_input = True
sum = 0
while continue_input:
    input_elements = input("Input numbers: ")
    input_list = input_elements.split()
    for val in input_list:
        if val == 'n':
            print(sum)
            print("Exit")
            exit(0)
        sum += float(val)
    print(sum)
    check = input("Continue? (y/n): ")
    if str.lower(check) == 'y':
        ...
    elif str.lower(check) == 'n':
        continue_input = False
        print("Exit")
        break
    else:
        print("Wrong answer. Exit")
        break
