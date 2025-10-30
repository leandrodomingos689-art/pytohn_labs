import json
import csv
from typing import List, Dict, Any

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    try:
        # Ler o arquivo JSON
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # Verificar se é uma lista de dicionários
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("O JSON deve ser uma lista de dicionários")
        
        if not data:
            # Se a lista estiver vazia, criar arquivo CSV vazio
            with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
                pass
            return
        
        # Coletar todos os campos únicos de todos os objetos
        all_fields = set()
        for item in data:
            all_fields.update(item.keys())
        
        # Ordenar campos (pode ser alfabético ou pela ordem do primeiro objeto)
        # Aqui usamos ordem alfabética conforme sugerido
        fieldnames = sorted(all_fields)
        
        # Escrever o arquivo CSV
        with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Escrever cabeçalho
            writer.writeheader()
            
            # Escrever dados, preenchendo campos faltantes com strings vazias
            for item in data:
                # Garantir que todos os campos estejam presentes
                row = {field: item.get(field, '') for field in fieldnames}
                writer.writerow(row)
                
    except Exception as e:
        raise Exception(f"Erro na conversão JSON para CSV: {str(e)}")

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    try:
        data = []
        
        # Ler o arquivo CSV
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            
            # Verificar se há cabeçalho
            if reader.fieldnames is None:
                raise ValueError("O arquivo CSV deve ter cabeçalho")
            
            # Ler todas as linhas
            for row in reader:
                # Converter todos os valores para string (como especificado)
                string_row = {key: str(value) if value is not None else "" for key, value in row.items()}
                data.append(string_row)
        
        # Escrever o arquivo JSON
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise Exception(f"Erro na conversão CSV para JSON: {str(e)}")


    sample_data = [
        {"nome": "João", "idade": 30, "cidade": "São Paulo"},
        {"nome": "Maria", "idade": 25, "país": "Brasil"},
        {"nome": "Carlos", "cidade": "Rio de Janeiro", "profissão": "Engenheiro"}
    ]
    
    # Salvar dados de exemplo em JSON
    with open('exemplo.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    # Testar conversão JSON para CSV
    json_to_csv('exemplo.json', 'exemplo.csv')
    print("Conversão JSON → CSV concluída!")
    
    # Testar conversão CSV para JSON
    csv_to_json('exemplo.csv', 'exemplo_de_volta.json')
    print("Conversão CSV → JSON concluída!")
    
    # Mostrar conteúdo dos arquivos gerados
    print("\nConteúdo do CSV:")
    with open('exemplo.csv', 'r', encoding='utf-8') as f:
        print(f.read())
    
    print("Conteúdo do JSON convertido:")
    with open('exemplo_de_volta.json', 'r', encoding='utf-8') as f:
        print(f.read())