import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.text import normalize, tokenize, count_freq, top_n

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёмкость"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

tokens = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tokens)
top = top_n(freq, 2)
print(f"Tokens: {tokens}")
print(f"Frequências: {freq}")
print(f"Top 2: {top}")
