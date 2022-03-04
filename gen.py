import time 

from matplotlib import pyplot as plt 

seed = int(time.time()*time.time_ns())%(10**5)
print(seed)

x = []

for i in range(10):

    seed = int(str(seed**2)[:5])

    rn = int(str(seed)[1:3])
    x.append(rn)

print(x)

plt.hist(x)
plt.show()

