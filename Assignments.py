#   CSV File handling

# 1. Write student data into a CSV fileimport csv

f = open("students.csv", "w", newline="")
w = csv.writer(f)
n = int(input("Enter number of students: "))
w.writerow(["Roll No", "Name", "Marks"])
for i in range(n):
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    w.writerow([roll, name, marks])

f.close()
print("Data written successfully")

# 2. Read all records from a CSV file

import csv

f = open("students.csv", "r")
r = csv.reader(f)

for row in r:
    print(row)

f.close()

# 3. Search a student record by name

import csv

f = open("students.csv", "r")
r = csv.reader(f)
name = input("Enter student name to search: ")
found = False
for row in r:
    if row[1] == name:
        print("Record found:", row)
        found = True
        break

if found == False:
    print("Record not found")
f.close()


# 4. Count total number of records in CSV file
import csv

f = open("students.csv", "r")
r = csv.reader(f)

count = 0
for row in r:
    count += 1

print("Total records:", count-1)   # excluding header

f.close()

# 5. Delete a student record from CSV file
import csv
f = open("students.csv", "r")
r = csv.reader(f)

name = input("Enter student name to delete: ")

rows = []
for row in r:
    if row[1] != name:
        rows.append(row)
f.close()

f = open("students.csv", "w", newline="") 
w = csv.writer(f)
w.writerows(rows)
f.close()


### Text File Handling
# Count vowels in a text file
f = open("data.txt", "r")
text = f.read()

count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("Total vowels:", count)
f.close()