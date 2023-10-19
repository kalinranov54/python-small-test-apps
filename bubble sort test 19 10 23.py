def bubble_sort(a):
    for i in range(0, len(a)-1):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                c = a[j]
                a[j] = a[j+1]
                a[j+1] = c
    return a


print("Input 10 numbers")
x1 = input()
x2 = input()
x3 = input()
x4 = input()
x5 = input()
x6 = input()
x7 = input()
x8 = input()
x9 = input()
x10 = input()
arr = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

print("sorting done")
print(bubble_sort(arr))

