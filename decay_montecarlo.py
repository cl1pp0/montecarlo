#!/usr/bin/python3
import random
import math
import matplotlib.pyplot as plt

# initial number of elements
n0 = 100

# remaining number of elements
n = n0

# decay rate, probability of decay per time unit
lambd = 1e-2
print("decay rate = %.2f" % lambd)

# theoretical halflife
halflife = 1/lambd*math.log(2)
print("halflife = %.2f" % halflife)

# halflife counter
nh = 2

# result lists
tlist = []
nlist = []
tdlist = []
dlist = []

# interval for delta decays
td = 10

# number of decays within td
d = 0

# print sample point 
def print_sample(t, n, c=""):
    print("t =%4.d, n =%4.d (%6.2f %%)" % (t, n, n/n0*100), c)

# init PRNG (you may want to use a fixed seed for reproducibility)
random.seed()

# time loop
for t in range(1000000):
    # number of decays per time unit
    nd = 0
    # sum up elements which decay in this time unit
    for i in range(n):
        if random.random() < lambd:
            nd += 1
    # substract decayed from remaining
    n -= nd
    # sum for delta decays figure
    d += nd
    # print if remaining elements are halved
    if n <= n0/nh:
        c = "1/" + str(nh)
        print_sample(t, n, c)
        nh *= 2
    # print and append sample with interval td
    elif t%td == 0:
        print_sample(t, n)
    if t%td == 0:
        tlist.append(t)
        nlist.append(n)
        if t > 0:
            tdlist.append(t)
            dlist.append(d)
            d = 0
    # print last sample
    if n == 0:
        print_sample(t, n)
        break

# plot graphs
plt.figure()
plt.plot(tlist, nlist, ".")
plt.show(block=False)

plt.figure()
plt.plot(tdlist, dlist, "x-")
plt.show()
