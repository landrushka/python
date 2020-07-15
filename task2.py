# Так как в условии не сказано о необходимости проверки входных данных, то она не реализована, поэтому предполагается
# что пользователь вводит данные корректно
input_seconds = int(input("Введите время в секундах: "))
seconds = input_seconds % 60
input_minutes = input_seconds // 60
minutes = input_minutes % 60
hours = input_minutes // 60
if seconds < 10:
    seconds = '0' + str(seconds)
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)
print('{hh}:{mm}:{ss}'.format(hh=hours, mm=minutes, ss=seconds))
