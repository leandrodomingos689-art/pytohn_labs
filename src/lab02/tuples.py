def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3 or not isinstance(rec, tuple):
        raise ValueError("Необходимо указать три параметра или должен быт tuple")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise ValueError("Nome incorreto ou Grupo deve ser string")
    if not isinstance(gpa, float):
        raise ValueError("GPA deve ser de digito decimal")
    # Processar FIO - remover espaços extras e dividir
    partes_nome = fio.strip().split()
    # Formar iniciais
    iniciais = []
    for parte in partes_nome[1:]:  # Pular sobrenome
        if parte:  # Se não estiver vazio
            iniciais.append(parte[0].upper() + ".")
    # Juntar sobrenome com iniciais
    nome_formatado = partes_nome[0].upper() + " " + " ".join(iniciais)
    # Formatar GPA com 2 casas decimais
    gpa_formatado = f"{gpa:.2f}"
    # Retornar string formatada
    return f"{nome_formatado}, гр. {group}, GPA {gpa_formatado}"


estudante1 = ("   Laurindo David Goncalo", "BIVT-25", 4.7)
print(format_record(estudante1))
