def zigzag():
    list = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']  # list containing symbols
    count = 0
    for i in list:#iterate thru the length of the list
        for j in range(5):
            if (j-count == 0 or j+count == 8): #count will know how many time it iterates thru the loop
                print("*", end="")
            else:
                print(end=" ")
        print()
        count += 1

for k in range(3):
    zigzag()


