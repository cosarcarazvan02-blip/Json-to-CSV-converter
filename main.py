import sys
import json
if len(sys.argv) != 3:
    print("Usage: python main.py input.json output.csv")
    sys.exit(1)
print("Arguments OK")
input_path=sys.argv[1]
output_path=sys.argv[2]
with open(input_path, "r", encoding="utf-8") as f:
    data=json.load(f)

print("Loaded", len(data), "records")

with open(output_path, "w", encoding="utf-8") as f:
    headers = data[0].keys()
    f.write(",".join(headers) + "\n")
    for record in data:
        row = [str(record[h]) for h in headers]
        f.write(",".join(row) + "\n")


