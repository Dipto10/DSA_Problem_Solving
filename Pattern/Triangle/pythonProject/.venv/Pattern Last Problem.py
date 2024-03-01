i = 1

n = int(input("Enter a numbers:"))

while i<=n:
    j = 1

    while j<=n-i+1:
        print(j, end=" ")
        j= j+1

    star = 2*i-2
    while star:
        print("*", end=" ")
        star = star-1

    k = n-i+1
    while k>=1:
        print(k, end=" ")
        k= k-1

    print()
    i = i+1







