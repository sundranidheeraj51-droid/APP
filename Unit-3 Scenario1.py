import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

with open(args.filename, "r") as file:
    data = list(csv.DictReader(file))

print("All Equipment Information:")
for row in data:
    print(row)

eid = input("\nEnter Equipment ID to search: ")

found = False
for row in data:
    if row["Equipment ID"] == eid:
        print("Equipment Found:")
        print(row)
        found = True
        break

if not found:
    print("Equipment not found")
