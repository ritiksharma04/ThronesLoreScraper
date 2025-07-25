import csv
import os

def save_to_csv(data, filepath):
    if not data:
            print("no data")
            return

    #making data directory
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    headers = data[0].keys()
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        d = csv.DictWriter(f,fieldnames=headers)
        d.writeheader()

        for item in data:
             d.writerow(item)
             
