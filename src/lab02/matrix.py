def transpose(mat: list[list[float | int]]) -> list[list]: #Transpõe a matriz (troca linhas por colunas)
   
    # Caso da matriz vazia
    if not mat:
        return []
    # Verificar se a matriz é retangular (todas as linhas têm o mesmo comprimento)
    primeira_linha_len = len(mat[0])
    for linha in mat:
        if len(linha) != primeira_linha_len:
            raise ValueError("Матрица должна быть «квадратной» — строки имеют разную длину.")
    # Criar matriz transposta
    num_linhas = len(mat)
    num_colunas = len(mat[0])
    # Inicializar matriz resultado com zeros
    resultado = []
    for j in range(num_colunas):
        nova_linha = []
        for i in range(num_linhas):
            nova_linha.append(mat[i][j])
        resultado.append(nova_linha)
    return resultado
#############################################################
def row_sums(mat: list[list[float | int]]) -> list[float]:
    # Caso da matriz vazia
    if not mat:
        return []
    # Verificar se a matriz é retangular
    primeira_linha_len = len(mat[0])
    for linha in mat:
        if len(linha) != primeira_linha_len:
            raise ValueError("Матрица должна быть «квадратной» — строки имеют разную длину.")
    # Calcular soma de cada linha
    resultado = []
    for linha in mat:
        soma = 0
        for elemento in linha:
            soma += elemento
        resultado.append(soma)
    return resultado
###############################################################
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Calcula a soma de cada coluna da matriz
    """
    # Caso da matriz vazia
    if not mat:
        return []
    
    # Verificar se a matriz é retangular
    primeira_linha_len = len(mat[0])
    for linha in mat:
        if len(linha) != primeira_linha_len:
            raise ValueError("Матрица должна быть «квадратной» — строки имеют разную длину.")
    
    # Calcular soma de cada coluna
    num_colunas = len(mat[0])
    resultado = []
    
    for j in range(num_colunas):
        soma = 0
        for i in range(len(mat)):
            soma += mat[i][j]
        resultado.append(soma)
    
    return resultado

print(transpose([[7,3], [8,4], [9,0]]))
print(row_sums([[1,2,3],[4,5,6]]))
print(col_sums([[1,2,3],[4,5,6]]))

