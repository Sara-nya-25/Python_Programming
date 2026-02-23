import csv
# Setup for creating the data
def initialize_inventory_file(filename, headers):
    """Creates the CSV file with default data if it doesn't exist."""
    raw_data = [
        ["MIL001", "Milk 3%", 26.90, 500],
        ["MIL002", "Milk Eko", 28.90, 300],
        ["MIL003","Milk 1.5%" ,21.9,200],
        ["EGG001", "Egg", 48.99, 300],
        ['HCHK88', 'Full Chicken', 89.99, 75],
        ['BRCHK99', 'Chicken Breast', 119.9, 45],
        ['FRPIN01', 'Pineapple', 35],
        ['FRBANA1', 'Banana Eko', 28.9],
        ['FRAPP02', 'Apple Royal Gala', 32.9],
        ['FRGRAP1', 'Grapes', 80, 300],
        ['VEGTOM12', 'Tomato', 52.9, 125],
        ['VEGCAR14', 'Carrot', 20, 300],
        ['VEGCUCU8', 'Cucucmber', 15, 400],
        ['VEGONI21', 'Onion', 16.9, 500],
        ['VEGGARL9', 'Garlic', 149.9, 100],
        ['COCOMB11', 'Marabou Milk chocolate', 38.9, 550],
        ['COCOFAZ1', 'Fazer Coco Nut', 50.9, 400],
        ["VEGGIN3", "Ginger", 69.90, 85],
        ["COCOMR3", "Marabou Hazelnut", 45.90, 350],
        ["COCOMR4", "Marabou White Cranberry", 52.90, 250]
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(raw_data)
    print(f"System: '{filename}' initialized successfully.")


