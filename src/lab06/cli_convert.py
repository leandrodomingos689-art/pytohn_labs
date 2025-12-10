import argparse
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="File conversion")
    # Creating commands: creating support for subcommands.
    # Subcommands will be stored in the "cmd" attribute.
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    # Argument "--in" required and stored in the "input" attribute.
    p1.add_argument("--in", dest="input", required=True)
    # Argument "--out" required and stored in the "output" attribute.
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()
    """
    Мы вызываем код в зависимости от аргументов..
    """
    if args.cmd == "json2csv":  # JSON to CSV conversion
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":  # CSV to JSON conversion
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":  # CSV to XLSX conversion
        csv_to_xlsx(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
