list = [0,1,2,3,4,5,6,7,8,9] #list containing list of  elements which specify number of times it has iterated thru the loop
for k in range(3):
    for i in list:#iterate thru the length of the list
        for j in range(5):#iterate thruf half the list  because it reverse at half so have to look at only 5.
            if j-i == 0 or j+i == 8:#correlate the j and i value to give it 0 or 8 and only print * if its true and space if its false
                print("*", end="")
            else:
                print(end=" ")
        print()#indent to new line

