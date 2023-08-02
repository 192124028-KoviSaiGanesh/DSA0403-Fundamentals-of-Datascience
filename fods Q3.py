import numpy as np
a=np.array([[1,2,r82000],[5,5,50000],[3,7,75000],[6,3,25000]])
bedrooms=a[:,0]
print(bedrooms)
ho=a[bedrooms>4]
av=np.mean(ho[:,2])
print(av)
