import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import tokenize, count_freq, top_n

if __name__ == "__main__":
    
    text = input("Digite ou cole um texto:\n> ")
    words = tokenize(text)
    freqs = count_freq(words)
    top = top_n(freqs, 5)

    print(f"\nTotal de palavras: {len(words)}")
    print(f"Palavras únicas: {len(freqs)}\n")
    print("Top 5 palavras mais frequentes:")

    for word, count in top:
        print(f"{word}: {count}")