import csv
from collections import defaultdict
from statistics import mean

# === BUGS ===

# === 1. Read products.csv into df using pandas ===
def read_csv_manual(path):
    data = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data  


# === 2. Better method?  ===
def groupby_category(data):
    categories = defaultdict(list)
    for row in data:
        categories[row['category']].append(float(row['price']))
    return {k: mean(v) for k, v in categories.items()}  

# === 3. Fill missing data  of a specific column with zeros ===
def fill_missing_manual(data, col):
    for row in data:
        if not row[col]:
            row[col] = 0

# === 4. Hint:Use List Comprehension ===
def add_discount_column(data):
    for row in data:
        row['discounted'] = float(row['price']) * 0.9

# === 5. Sort in descending order ===
def sort_by_price(data):
    return sorted(data, key=lambda x: float(x['price']), reverse=True)

# === 6 .It's 2025, and you're still manually coding pivot tables? ===
def manual_pivot(data, index_col, columns_col, values_col):
    pivot = defaultdict(dict)
    index_vals = set()
    col_vals = set()
    
    for row in data:
        idx = row[index_col]
        col = row[columns_col]
        val = float(row[values_col])
        index_vals.add(idx)
        col_vals.add(col)
        pivot[idx][col] = val
    
    columns = sorted(col_vals)
    result = []
    for idx in sorted(index_vals):
        row = {'index': idx}
        for col in columns:
            row[col] = pivot[idx].get(col, 0)
        result.append(row)
    return result
