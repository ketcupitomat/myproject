import re
import json


def clean_price(price_str):
    """
    Convert price like '1 200,00' → 1200.00
    """
    price_str = price_str.replace(" ", "").replace(",", ".")
    return float(price_str)


def parse_receipt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    products = []
    prices = []
    total_amount = None
    payment_method = None
    date = None
    time = None

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Detect product number like "1."
        if re.match(r"^\d+\.$", line):
            # Next line is product name
            product_name = lines[i + 1].strip()
            products.append(product_name)

            # Price line is usually 2 lines below
            price_line = lines[i + 3].strip()

            price_match = re.search(r"[\d\s]+,\d{2}", price_line)
            if price_match:
                price = clean_price(price_match.group())
                prices.append(price)

            i += 4
            continue

        # Detect TOTAL
        if "ИТОГО" in line.upper():
            total_match = re.search(r"[\d\s]+,\d{2}", lines[i + 1])
            if total_match:
                total_amount = clean_price(total_match.group())

        # Detect payment method
        if "БАНКОВСКАЯ КАРТА" in line.upper():
            payment_method = "CARD"

        # Detect date and time
        datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}", line)
        if datetime_match:
            date = datetime_match.group()

        time_match = re.search(r"\d{2}:\d{2}:\d{2}", line)
        if time_match:
            time = time_match.group()

        i += 1

    # If total not found, calculate
    if total_amount is None:
        total_amount = sum(prices)

    return {
        "products": products,
        "prices": prices,
        "total_amount": total_amount,
        "payment_method": payment_method,
        "date": date,
        "time": time
    }


if __name__ == "__main__":
    result = parse_receipt("raw.txt")

    print("\nParsed Receipt Data")
    print("=" * 40)
    print(json.dumps(result, indent=4, ensure_ascii=False))