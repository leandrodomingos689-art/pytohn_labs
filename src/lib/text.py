import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    result = text
    if casefold:
        result = result.casefold()
    if yo2e:
        result = result.replace('ё', 'e').replace('Ё', 'E')
    control_chars = ['\t', '\r', '\n']
    for char in control_chars:
        result = result.replace(char, ' ')
    result = ' '.join(result.split())
    return result

def tokenize(text: str) -> list[str]:
    """
    Divide o texto em palavras/tokens usando expressão regular.
    """
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Retorna os N tokens mais frequentes, ordenados por frequência e alfabeticamente.
    """
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[:n]