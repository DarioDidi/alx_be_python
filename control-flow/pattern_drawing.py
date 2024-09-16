size = int(input("Enter the size of the pattern:"))
row = size + 0
while size > 0:
    for j in range(size):
        print("*", end="")
    print("\n")
    size -= 1



