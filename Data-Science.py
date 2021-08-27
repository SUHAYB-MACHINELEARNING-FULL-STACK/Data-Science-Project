import matplotlib.pyplot as plt

from random import randint as s

arr1 = []

for i in range(10): 
	for x in range(s(1,s(1,1000))): 
		arr1.append(i)
		
plt.hist(arr1)

# Display histogram
plt.show()