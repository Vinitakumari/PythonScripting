"""l1= [3,5,9,8,3,4,5,9,6,3,7,2]
l2 =[]

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)
"""

L1 = [3,5,9,8,3,4,5,9,6,3,7,2]

seen = set()
L1[:]= [ item for item in L1 if not  (item in seen or seen.add(item))]
print(L1)