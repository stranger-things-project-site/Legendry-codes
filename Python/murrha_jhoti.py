n = int(input("Enter any integer :- "))
fact = 1
for i in range(1, n + 1):
    if n == 0 or n == 1:
        print(1)
        exit
    else:
        fact *= i
print(fact)
