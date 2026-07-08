# import pickle
## non - readable 
## size 
## data type retain 

## wb , rb , ab
# example 1
# write
# import pickle

# file1 = open("student.bin","wb" )
# n = int(input("enter "))
# studentlist = [] 
# for i in range(n):
#     rollno = int(input("enter roll no "))
#     name = input("enter name ")
#     per = float(input("enter percentage "))
#     studentlist.append([rollno, name, per])

# pickle.dump(studentlist, file1)
# file1.close()
### with###################
# with open("student.bin","wb" ) as file1 : 
#     n = int(input("enter "))
#     studentlist = [] 
#     for i in range(n):
#         rollno = int(input("enter roll no "))
#         name = input("enter name ")
#         per = float(input("enter percentage "))
#         studentlist.append([rollno, name, per])

#     pickle.dump(studentlist, file1)

################################
# import pickle 
# with open("student.bin", "rb") as file1:
#     list1 = pickle.load(file1)
#     for i in list1:
#         print(i)
######################################################
# 2025
import pickle 
def create():
    with open("passanger.dat" ,"ab") as file1:
        list1= []
        n = int(input("enter no of students "))
        for i in range(n):
            pnr = input("Enter pnr ")
            pname = input("Enter pname ")
            brdstn = input("enter Boarding ")
            destn = input("enter destination ")
            fare = float(input("enter fare ") )
            list1.append([pnr, pname, brdstn, destn, fare])
        pickle.dump(list1, file1)
def searchdestn(D):
    try:
        with open("passanger.dat" ,"rb") as file1:
            list1 = pickle.load(file1)
            for i in list1:
                if i[3]==D:
                    print(i)
    except:
        print("End of the File ")
    
        
    
    