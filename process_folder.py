from pathlib import Path
import json

def calculate_material_cost(weight_grams, price_per_kg):
    price = (weight_grams / 1000) * price_per_kg
    return price

folder_path = Path("orders_folder")
results = []

for file_path in folder_path.glob("*.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    calc = calculate_material_cost(data["weight"], data["price_per_kg"])
    results.append({"patient": data["patient"], "cost": calc})

with open("total_report.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)
    