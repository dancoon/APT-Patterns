for i in range(4):
    for j in range(4):
        if i == 0 or i == 3:
            print("*", end=" ")
        else:
            if j == i:
                print("*", end=" ")
            else:
                print("&", end=" ")
        
    print()