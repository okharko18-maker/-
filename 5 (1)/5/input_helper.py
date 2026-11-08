"""Наданий helper: лише перетворення на скінченний float."""
import math
def read_finite_float(prompt):
    while True:
        text=input(prompt)
        try: value=float(text)
        except ValueError:
            print("Помилка: введіть число")
            continue
        if not math.isfinite(value):
            print("Помилка: nan та нескінченності не дозволені")
            continue
        return value
