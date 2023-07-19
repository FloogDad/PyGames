for i in range(99, 0, -1):
    print(str(i)+(" bottle" if i == 1 else " bottles") +" of juice on the wall, "+str(i)+(" bottle" if i == 1 else " bottles") +" of juice.")
    print("Take one down and pass it around, "+str(i-1)+ (" bottle" if i == 2 else " bottles") +" of juice on the wall.\n")
