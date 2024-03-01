i = 1
n = int(input("Enter a number:"))

while i<=n:
    space = i-1
    while space:
        print(" ", end =" ")
        space = space-1
    j = 1

    while j<=n-i+1:
        print("x", end=" ")
        j = j+1
    print()
    i = i+1


