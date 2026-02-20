import csv
# Setup for creating the data
def initialize_inventory_file(filename, headers):
    """Creates the CSV file with default data if it doesn't exist."""
    raw_data = [
        ["MIL001", "Milk 3%", 26.90, 500],
        ["MIL002", "Milk Eko", 28.90, 300],
        ["EGG001", "Egg", 48.99, 300],
        ["VEGGIN3", "Ginger", 69.90, 85],
        ["COCOMR3", "Marabou Hazelnut", 45.90, 350],
        ["COCOMR4", "Marabou White Cranberry", 52.90, 250]
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(raw_data)
    print(f"System: '{filename}' initialized successfully.")


