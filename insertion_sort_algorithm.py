A = [8,4,3,7,1,5,9]

# Slowest double nested loops
def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break
        return A

# Insertion algorithm using while
def insertion_sort_while(A):
    for i in range(1, len(A)):
        j = i-1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A

# Insertion sort
def insertion_sort__refactored(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1, -1, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break
    return A

print(A, "unsorted arr")
print(insertion_sort(A), "sorted arr")
print(insertion_sort_while(A), "sorted arr while")
print(insertion_sort__refactored(A), "sorted arr refactor")

def is_divisible(A):
    for i in range(1, len(A)):
        if A[i] == 9 :
            num = A[i] - 1
            return num, "TEST"

print(is_divisible(A), "divisible")

str = "level"
str_2 = "carlos"

def is_palindrom(str_2):
    
