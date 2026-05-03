import csv
import os

def save_report(results):
    os.makedirs("data", exist_ok=True)
    filepath = "data/test_report.csv"
    if not results:
        return
        
    keys = results[0].keys()
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)