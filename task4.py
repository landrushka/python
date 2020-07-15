n_str = input("Введите число: ")
idx = 1
idx_max = 0
max = n_str[idx_max]
while idx < n_str.__len__():
    if n_str[idx] > max:
        idx_max = idx
        max = n_str[idx_max]
    idx += 1

print(max)
