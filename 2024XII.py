# Q21
# A (A) Write a user defined function in Python named
# showGrades (S) which takes the dictionary S as
# an argument. The dictionary, S contains Name:
# [Eng ,Math, Science] as key: value pairs. The
# function displays the corresponding grade
# obtained by the students according to the
# following grading rules: 2
# Average of Eng ,Math , Science Grade
            # >=90 A
            # <90 but >=60 B
            # <60 C
# For example: Consider the following dictionary
# S={“AMIT”: [92, 86, 64], “NAGMA”: [65, 42, 43],
# “DAVID”: [92, 90, 88]}
# The output should be:
# AMIT – B
# NAGMA – C
# DAVID – A

def showGrades(S):
    for name, grades in S.items():
        average = sum(grades) / len(grades)
        if average >= 90:
            grade = 'A'
        elif average >= 60:
            grade = 'B'
        else:
            grade = 'C'
        print(f"{name} - {grade}")  


# Write a user defined function in Python named
# Puzzle (W, N) which takes the argument W as an
# English word and N as an integer and returns the
# string where every Nth alphabet of the word W is
# replaced with an underscore ( “_”).
# For example: if W contains the word “TELEVISION”
# and N is 3, then the function should return the
# string “TE_EV_SI_N”. Likewise for the word
# “TELEVISION” if N is 4, then the function should
# return “TEL_VIS_ON”.

def Puzzle(W, N):
    result = ""
    for i in range(len(W)):
        if (i + 1) % N == 0:
            result += "_"
        else:
            result += W[i]
    return result  
print(Puzzle("TELEVISION", 3))  # Output: TE_EV_SI_N
print(Puzzle("TELEVISION", 4))  # Output: TEL_VIS_ON
