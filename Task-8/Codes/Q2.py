import numpy as np

lst1 = [] 
lst2 = [] 
 
lst1 = [int(item) for item in input("First Array : ").split()]
lst2 = [int(item) for item in input("Second Array : ").split()]

lst1 = np.array(lst1)
lst2 = np.array(lst2)

comparison = lst1 == lst2
equal_arrays = comparison.all()
  
print(equal_arrays)