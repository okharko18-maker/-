
import math


# Дозволені класи автомобілів
VALID_CLASSES = ["економ", "комфорт", "бізнес"]


# Завантаження та перевірка записів
def load_records(lines):
    records = []
    errors = []

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        if not line:
            continue

        fields = line.split(";")

        # Перевірка кількості полів
        if len(fields) != 5:
            errors.append(
                f"Рядок {line_number}: Неправильна кількість полів"
            )
            continue

        brand, car_class, days, price_per_day, insurance = fields

        brand = brand.strip()
        car_class = car_class.strip()
        insurance = insurance.strip()

        # Перевірка класу автомобіля
        if car_class not in VALID_CLASSES:
            errors.append(
                f"Рядок {line_number}: Невідомий клас авто"
            )
            continue

        # Перевірка числових даних
        try:
            days = int(days)
            price_per_day = float(price_per_day)

            if days <= 0 or price_per_day <= 0:
                raise ValueError

            if not math.isfinite(price_per_day):
                raise ValueError

        except ValueError:
            errors.append(
                f"Рядок {line_number}: Некоректні числові дані"
            )
            continue

        # Перевірка страхування
        if insurance not in ["так", "ні"]:
            errors.append(
                f"Рядок {line_number}: Некоректне значення страхування"
            )
            continue

        # Обчислення загальної вартості
        total_price = days * price_per_day

        if insurance == "так":
            total_price *= 1.1

        # Створення запису
        record = {
            "brand": brand,
            "car_class": car_class,
            "days": days,
            "price_per_day": price_per_day,
            "insurance": insurance,
            "total_price": total_price
        }

        records.append(record)

    return records, errors


# Підрахунок статистики за класами автомобілів
def summarize(records):
    result = {}

    for record in records:
        car_class = record["car_class"]
        price = record["total_price"]

        if car_class not in result:
            result[car_class] = {
                "count": 0,
                "total": 0.0,
                "average": 0.0,
                "max": 0.0
            }

        result[car_class]["count"] += 1
        result[car_class]["total"] += price

        if price > result[car_class]["max"]:
            result[car_class]["max"] = price

    # Обчислення середньої вартості
    for car_class in result:
        count = result[car_class]["count"]
        total = result[car_class]["total"]

        result[car_class]["average"] = total / count

    return result


# Пошук унікальних марок автомобілів
def unique(records):
    result = []
    seen_brands = set()

    for record in records:
        brand = record["brand"]

        if brand not in seen_brands:
            result.append(record)
            seen_brands.add(brand)

    return result


# Пошук найдорожчих оренд
# Для кожної марки враховується один найдорожчий запис
def top_n(records, n):
    best_by_brand = {}

    for record in records:
        brand = record["brand"]

        if (
            brand not in best_by_brand
            or record["total_price"] >
            best_by_brand[brand]["total_price"]
        ):
            best_by_brand[brand] = record

    sorted_records = sorted(
        best_by_brand.values(),
        key=lambda record: record["total_price"],
        reverse=True
    )

    return sorted_records[:n]


# Основна частина програми
if __name__ == "__main__":

    # Вхідні дані
    data = [
        "Toyota;економ;3;1000.0;ні",
        "BMW;бізнес;2;3000.0;так",
        "Audi;люкс;2;3000.0;так",
        "Skoda;економ;5;900.0;так",
        "Ford;економ;-1;1000.0;ні"
    ]

    # Завантаження записів
    records, errors = load_records(data)

    print("ПРАВИЛЬНІ ЗАПИСИ:")

    for record in records:
        print(record)

    # Виведення помилок
    print("\nПОМИЛКИ:")

    for error in errors:
        print(error)

    # Статистика
    statistics = summarize(records)

    print("\nЗВІТ ЗА КЛАСАМИ:")

    for car_class, values in statistics.items():
        print(
            f"Клас {car_class}: записів {values['count']}, "
            f"загальна вартість {values['total']:.2f}, "
            f"сер. вартість {values['average']:.2f}, "
            f"макс. вартість {values['max']:.2f}"
        )

    # Загальна кількість оренд
    print(f"\nВсього оренд: {len(records)}")

    # Унікальні марки
    print("\nУНІКАЛЬНІ МАРКИ:")

    for record in unique(records):
        print(record["brand"])

    # Три найдорожчі оренди різних марок
    print("\nТОП-3 НАЙДОРОЖЧИХ ОРЕНД:")

    for record in top_n(records, 3):
        print(
            record["brand"],
            f"{record['total_price']:.2f}"
        )
