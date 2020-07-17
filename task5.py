my_list = [7, 5, 3, 3, 2]
continue_input = True

while continue_input:
    input_element = int(input("Input integer: "))
    for idx, element in enumerate(my_list):
        if input_element >= element:
            my_list.insert(idx, input_element)
            break
        elif idx == len(my_list) - 1:
            my_list.insert(idx + 1, input_element)
            break
    print("Пользователь ввел число {input_element}. Результат:{my_list}".format(input_element=input_element,
                                                                                my_list=my_list))
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
