sample_data = [(1,2),3,[4,5],6]
for i in sample_data:
    if (type ( i ) is list )or (type ( i ) is tuple):
        for j in i:
            print(j,end=" ")
    else:
        print( i, end=" ")
