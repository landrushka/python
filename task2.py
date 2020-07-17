input_list = list()
continue_input = True

while continue_input:
    input_element = input("Input any value: ")
    input_list.append(input_element)
    check = input("Continue? (y/n): ")
    if str.lower(check) == 'y':
        ...
    elif str.lower(check) == 'n':
        continue_input = False
        print("Input elements: ", input_list)
    else:
        print("Wrong answer. Exit")
        print("Input elements: ", input_list)
        break

len_input_list = len(input_list)

for idx in range(0, len_input_list - 1, 2):
    temp = input_list[idx]
    input_list[idx] = input_list[idx + 1]
    input_list[idx + 1] = temp

print("Output elements: ", input_list)
