from pathlib import Path
import csv

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """""
    encoding="cp1251"
    """""
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: list [tuple|list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

