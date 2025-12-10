from pathlib import Path
import json
import csv
from typing import List, Dict, Any


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    j = Path(json_path)
    if j.suffix.lower() != ".json":
        print("Erro!!! Ficheiro deve ser JSON!")
        return False
    try:
        # Прочитать JSON-файл
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Verificar se é uma lista de dicionários
        # Проверьте, является ли это списком словарей.
        if not isinstance(data, list) or not all(
            isinstance(item, dict) for item in data
        ):
            raise ValueError("O JSON deve ser uma lista de dicionários")

        if not data:
            # Se a lista estiver vazia, criar arquivo CSV vazio
            # Если список пуст, создайте пустой CSV-файл.
            with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
                pass
            return

        # Coletar todos os campos únicos de todos os objetos
        # Соберите все уникальные поля из всех объектов.
        all_fields = set()
        for item in data:
            all_fields.update(item.keys())

        # Ordenar campos (pode ser alfabético ou pela ordem do primeiro objeto)
        # Сортировка полей (можно в алфавитном порядке или по порядку первого объекта)
        # Aqui usamos ordem alfabética conforme sugerido
        # Здесь мы используем алфавитный порядок, как и предлагается.

        fieldnames = sorted(all_fields)

        # Escrever o arquivo CSV
        # Запишите CSV-файл.
        with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Escrever cabeçalho
            # Написать заголовок
            writer.writeheader()

            # Escrever dados, preenchendo campos faltantes com strings vazias
            # Запись данных, заполнение пропущенных полей пустыми строками
            for item in data:
                # Garantir que todos os campos estejam presentes
                # Убедитесь, что все поля присутствуют
                row = {field: item.get(field, "") for field in fieldnames}
                writer.writerow(row)
            print("Преобразование JSON в CSV завершено!")
            return True
    except Exception as e:
        raise Exception(f"Ошибка преобразования JSON в CSV.: {str(e)}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    try:
        data = []

        # Прочитать CSV-файл
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            # Verificar se há cabeçalho
            # Проверяем заголовок
            if reader.fieldnames is None:
                print("CSV-файл должен иметь заголовок.")
                return False

            # Ler todas as linhas
            # Прочтите все строки
            for row in reader:
                # Converter todos os valores para string (como especificado)
                # Преобразовать все значения в строки (как указано)
                string_row = {
                    key: str(value) if value is not None else ""
                    for key, value in row.items()
                }
                data.append(string_row)

        # Escrever o arquivo Json
        # Запишите JSON-файлo
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print("Преобразование CSV в JSON завершено!")
        return True

    except Exception as e:
        raise Exception(f"Ошибка преобразования CSV в JSON.: {str(e)}")


# Testar conversão CSV para JSON
# Тестирование преобразования CSV в JSON
# csv_to_json("data/sample/people.csv", 'data/out/people_from_csv.json')
