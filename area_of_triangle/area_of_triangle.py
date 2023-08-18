def getTrianglearea(x, y):
    area = (x[0]*(y[1]-y[2]) + x[1]*(y[2]-y[0]) + x[2]*(y[0]-y[1]))
    
    a = abs(area/2)

    return int(a)