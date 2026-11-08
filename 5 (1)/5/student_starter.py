"""PP-LAB01 starter. Keep input_helper.py beside this file."""
import json, math, sys
from pathlib import Path
from input_helper import read_finite_float
if len(sys.argv)!=2 or not sys.argv[1].isdigit() or not 1<=int(sys.argv[1])<=30: raise SystemExit("Запуск: python student_starter.py НОМЕР_1_30")
card=json.loads(Path(__file__).with_name("student_variants.json").read_text(encoding="utf-8"))["variants"][int(sys.argv[1])-1]
print("Варіант:",card["number"],card["title"])
values={}
for spec in card["inputs"]:
    values[spec["name"]]=read_finite_float(f"{spec['label']}, {spec['unit']}: ")
# Доповніть отримання кожного числа власною перевіркою min/max і strictly_positive:
# після помилки повторіть запит, після успіху збережіть число.
# Потім обчисліть формулу без проміжного округлення. math.pi вже імпортовано.
print("TODO: додайте валідацію, формулу й результат свого варіанта")
