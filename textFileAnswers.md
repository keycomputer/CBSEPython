# Question 29 – 2025 
### a 
```
def displayVote():

     file1 = open("Elections.txt", "r")
     List1 = file1.readlines()
     for i in List1:
         List2 = i.split() ## list of words  in a sentence 
         if "vote" in List2 :
             print(i)
     file1.close()
```

### b 
```
def displayVowel():

     file1 = open("Report.txt", "r")
     str1 = file1.read() # read entire content-> return string in str1 
     list1 = str1.split() # word by word
     for i in list1:
         if i[0].lower() in "aeiou" and i[-1].lower() in "aeiou":  
         # if i[0] in "aeiouAEIOU" and i[-1]..........:
             print(i)
```
############################################################
# 2024
### Question 28
###  a 
```
def showInLines():
    f = open("STORY.txt" ,"r")
    str1 = f.read() # read entire content 
    for i in str1:
        if i=="." or i=="?" or i=='!' :
            print(i)
        elif i=="\n":
            print("", end="")
        else:
            print(i, end="")
showInLines()  
```

```
def c_words():
    countupper = 0
    countlower = 0 
    f = open("Wrods.txt","r")
    str1= f.read()
    for i in str1:
        if i.isupper() :
            countupper+=1
        elif i.islower():
            countlower+=1
    print("Count of Upper Letters ", countupper)
    print("Count of Lower Letters  ", countlower)
```