# outer loop for rows
for i in range(0,5):
    # inner loop for columns
    # values is changing according to outer loop
    for j in range(0,i+1):
        #print stars and staying on the same line after a print is done.
        print("* ", end="")
    print()#print new line
    #repeat step but with decreasing values for both loops
for i in range(5,0,-1):
    for j in range(i-1):
        print("* ", end="")
    print()