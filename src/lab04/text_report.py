import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from io_txt_csv import read_text, write_csv
from library.text import tokenize, count_freq, top_n, normalize

pathtxt = "data/lab04/a.txt"

pathCSV = "data/lab04/report.csv"

texto = read_text(pathtxt)

norma = normalize(texto)
token = tokenize(norma)
freq = count_freq(token)
top = top_n(freq)


write_csv(top, pathCSV, header=("word", "count"))

print(len(token))
print(len(freq))
print(top_n(freq))
