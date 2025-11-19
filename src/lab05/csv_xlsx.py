import csv
from openpyxl import Workbook
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    """
    # Проверка существования файла
    if not Path(csv_path).exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    
    # Проверка расширения
    if not csv_path.lower().endswith('.csv'):
        raise ValueError("Неверный тип файла: требуется .csv")
    
    # Чтение CSV и проверка на пустоту
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("CSV файл пуст")
    
    # Создание XLSX
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Запись данных
    for row in rows:
        ws.append(row)
    
    # Автоширина колонок
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        
        for cell in column:
            try:
                max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        
        adjusted_width = max(8, min(max_length + 2, 50))
        ws.column_dimensions[column_letter].width = adjusted_width
    
    # Сохранение
    wb.save(xlsx_path) 

#csv_to_xlsx("data/sample/people.csv", 'data/out/people.xlsx')