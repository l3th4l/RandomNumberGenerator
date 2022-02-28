import time 

from matplotlib import pyplot as plt 

seed = time.time()%(10**5)

x = []

for i in range(500):

    seed = int(str(seed**2)[:5])

    rn = int(str(seed)[1:3])
    x.append(rn)

    print(rn)

plt.hist(x)
plt.show()

