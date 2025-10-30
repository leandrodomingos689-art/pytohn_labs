def format_record(rec: tuple[str, str, float]) -> str:
   
    fio, group, gpa = rec
    # Processar FIO - remover espaços extras e dividir
    partes_nome = fio.strip().split()
    # Formar iniciais
    iniciais = []
    for parte in partes_nome[1:]:  # Pular sobrenome
        if parte:  # Se não estiver vazio
            iniciais.append(parte[0].upper() + ".")
    
    # Juntar sobrenome com iniciais
    nome_formatado = partes_nome[0] + " " + " ".join(iniciais)
    # Formatar GPA com 2 casas decimais
    gpa_formatado = f"{gpa:.2f}"
     # Retornar string formatada
    return f"{nome_formatado}, гр. {group}, GPA {gpa_formatado}"
# Testes
if __name__ == "__main__":
    # Teste 1: Nome completo (sobrenome + nome + patronímico)
    estudante1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
    print("Teste 1:", format_record(estudante1))
     # Teste 2: Nome sem patronímico
    estudante2 = ("Петров Алексей", "BIVT-23", 3.85)
    print("Teste 2:", format_record(estudante2))
     # Teste 3: Com espaços extras
    estudante3 = ("  Сидоров   Петр   ", "BIVT-24", 4.25)
    print("Teste 3:", format_record(estudante3))
    # Teste 4: GPA com muitas casas decimais
    estudante4 = ("Кузнецов Дмитрий Сергеевич", "BIVT-26", 3.789)
    print("Teste 4:", format_record(estudante4))
    # Teste 5: Nome com apenas uma parte (apenas sobrenome)
    estudante5 = ("Смирнов", "BIVT-22", 4.0)
    print("Teste 5:", format_record(estudante5))