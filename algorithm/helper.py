import numpy

def upshift(a,index,n):
    col = []
    for j in range(len(a)):
        col.append(a[j][index])
    shiftCol = numpy.roll(col,-n)
    # for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         if(j==index):
    #             a[i][j] = shiftCol[i]
    for i in range(len(a)):
        a[i][index] = shiftCol[i]

def downshift(a,index,n):
    col = []
    for j in range(len(a)):
        col.append(a[j][index])
    shiftCol = numpy.roll(col,n)
    # for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         if(j==index):
    #             a[i][j] = shiftCol[i]
    for i in range(len(a)):
        a[i][index] = shiftCol[i]


def rotate180(n):
    bits = "{0:b}".format(n) #int to bin
    return int(bits[::-1], 2) #reverse and convert bin to int
