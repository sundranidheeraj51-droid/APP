import csv
import argparse

p = argparse.ArgumentParser()
p.add_argument("filename")
a = p.parse_args()

with open(a.filename) as f:
    data = list(csv.DictReader(f))

for row in data:
    print(row)

id = input("Enter Course ID: ")

for row in data:
    if row["Course ID"] == id:
        print("Course Found:", row)
        break
else:
    print("Course not found")
