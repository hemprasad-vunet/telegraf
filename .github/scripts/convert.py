import json
import csv

input_file = "gitleaks-report.json"
output_file = "gitleaks-report.csv"

fields = [
    "Description", "File", "StartLine", "EndLine", "StartColumn", "EndColumn",
    "Match", "Secret", "Commit", "Author", "Email", "Date", "Message", "RuleID",
    "Entropy", "Fingerprint"
]

try:
    with open(input_file, "r") as json_file:
        data = json.load(json_file)

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        if isinstance(data, list):
            for entry in data:
                writer.writerow({field: entry.get(field, "") for field in fields})
except FileNotFoundError:
    print(f"Error: {input_file} not found.")
except json.JSONDecodeError:
    print(f"Error: Failed to decode JSON in {input_file}.")
