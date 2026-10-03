from pathlib import Path
import json
import pandas as pd

def calculate_material_cost(weight_grams, price_per_kg):
    price = (weight_grams / 1000) * price_per_kg
    return price

folder = Path('mixed_orders')
all_results = []

for item in folder.glob("*"):
    print(f"Найден файл: {item.name}, расширение: {item.suffix}")
    
    if item.suffix == ".json":
        with open(item, "r", encoding="utf-8") as file:
            data = json.load(file)
        for order in data:
            patient = order["patient"]
            weight = order["weight"]
            per_kg = order["price_per_kg"]
            calc = calculate_material_cost(weight, per_kg)
            if calc >= 2500:
                category = "дорогая печать"
            else:
                category = "дешёвая печать"
            all_results.append({"source": item.name, "patient": patient, "cost": calc, "category": category})
            
    elif item.suffix == ".xlsx":
        rd = pd.read_excel(item)
        data_2 = rd.to_dict('records')
        for order in data_2:
            patient = order["patient"]
            weight = order["weight"]
            per_kg = order["price_per_kg"]
            calc = calculate_material_cost(weight, per_kg)
            if calc >= 2500:
                category = "дорогая печать"
            else:
                category = "дешёвая печать"
            all_results.append({"source": item.name, "patient": patient, "cost": calc, "category": category})
            
print(all_results)
result = pd.DataFrame(all_results)
result.to_excel('final_report.xlsx', index=False)
print("Файл был успешно сохранён.")
print("\n---СТАТИСТИКА---")
c = result['cost'].sum() #Сумма всего
o = result['cost'].mean() #Среднее
r = result['cost'].max() #Максимум
max_row = result.loc[result['cost'].idxmax()]
most_expensive_patient = max_row['patient']
print(f"Общая сумма: {c}\nСреднее: {o}\nМаксимум: {r}\nСамый дорогой пациент: {most_expensive_patient}")

