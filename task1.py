my_list = [1, 1.1, '1', (), [], {}, True]

for idx, element in enumerate(my_list):
    if any([type(element) in [int, float, str, bool, tuple, list, dict]]):
        print("Type of {element!r} is {type} in my_list[{idx}]".format(element=element,
                                                                       type=type(element).__name__,
                                                                       idx=idx))
    else:
        print('Type of {element} not found'.format(element=element))
