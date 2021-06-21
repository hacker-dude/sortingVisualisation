import numpy
x = numpy.random.randint(low=1,high=100,size=30)
print(x)
for i in range(30):
    for j in range(0, 30 - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]

print(x)