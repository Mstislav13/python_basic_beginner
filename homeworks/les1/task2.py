time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время: {hours} часов: {minutes} минут: {seconds} секунд")

# Ещё один вариант перевода:
conversion = f"{time} секунд соответствует:\n {time/3600} часам,\n {time/60} минутам,\n {time} секундам."
print(conversion)