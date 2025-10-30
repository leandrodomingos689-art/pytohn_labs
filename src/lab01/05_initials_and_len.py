fio_input = input("ФИО: ").strip()

# Убираем лишние пробелы между словами
fio_clean = ' '.join(fio_input.split())

# Получаем инициалы
parts = fio_clean.split()
initials = ""

for part in parts:
    if part:  # Проверяем, что строка не пустая
        initials += part[0].upper()

# Выводим результат
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(fio_clean)}")

