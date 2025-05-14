"""d1 ={ 1:"one",2:"two",3: "three"}
print (d1)
print(d1[1])"""

# ways to create dictionary 
# iterable pairs

"""[(1,'one'),(2,'two'),(3,'three')] # list  containing tuples
d1 = dict([(1,'one'),(2,'two'),(3,'three')] )
print(d1)
"""
L1 = [1,2,4]
L2 =[3,8,7]
zip (L1,L2)
d2 =  dict(zip (L1,L2))
print(d2)