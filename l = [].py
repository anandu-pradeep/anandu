l = []
n = int(input("Enter total number of elements: "))


for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    l.append(value)


print("Even numbers in the list:")
for num in l:
    if num % 2 == 0:
        print(num)