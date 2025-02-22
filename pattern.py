def print_half_triangle(n):
    num=1
    for i in range(1,n+1):
        for j in range(1,i +1):
            print(num,end=" ")
            num+= 1
        print()
n = int(input("Enter the number of rows: "))
print_half_triangle(n)
