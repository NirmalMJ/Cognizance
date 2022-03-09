import numpy as np

n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

ary = np.array([i for i in range(n1,(n2+1),1)])
n = 5
d = np.zeros(len(ary)+((len(ary)-1)*n))
d[0:len(d):(n+1)] = ary

print(d)