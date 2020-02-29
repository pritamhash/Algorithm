def finder(ar1,ar2):
    #Sort the arrays
    ar1.sort()
    ar2.sort()
    for num1,num2 in zip(ar1, ar2):
        if num1!=num2:
            return num1
    return ar1[:-1]


ar1 = [1, 2, 3, 4, 5, 6, 7]
ar2 = [3, 7, 2, 1, 4, 6]
print(finder(ar1,ar2))


