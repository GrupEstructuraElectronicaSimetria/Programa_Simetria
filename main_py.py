import shp


print(shp.cshm.__doc__)

v = [[1, 2, 3],
     [4, 5, 6],
     [2, 4, 6],
     [1, 3, 5]]

print(shp.cshm(v,2))
print(shp.cshm(v,2,True))

print(shp.test(v,2))
print(shp.test(v,2,True))

print(shp.poly(v,2))
print(shp.poly(v,2,True))