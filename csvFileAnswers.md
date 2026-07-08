# 2025 -question 33 
```
import csv
def read_data():
    with open("P_record.csv", "r", newline="") as file1:
        reader = csv.reader(file1)
        for i in reader:
            if i[1].lower() == "cancer":
                print(i)


def count_rec():
    c = 0
    with open("P_record.csv", "r", newline="") as file1:
        reader = csv.reader(file1)
        for i in reader:
            count+=1 
    return c
```
2024
```


```
2023
```
def Courier_add():
    with open("courier.csv", "a", newline="") as file1:
        writer = csv.writer(file1)
        cid = int(input("enter cid))
        s_name = input("enter name")
        source = input("enter source ")
        destination = input("enter destination ")
        temp = [cid, s_name, source, destination]
        writer.writerow(temp)
 
def courier_serach():
    with open("courier.csv", "r", newline="") as file1:
        reader=  csv.reader(file1)
        destination = input("enter ")
        for i in reader:
            if i[3].lower() == destination:
               print(i)

```
