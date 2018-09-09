import sys

l=1
k=0
n=int(sys.argv[1])

mult=0
add=0

print("n is {}".format(n))

for i in range(1, n+1):
    l=.5*l*i
    mult=mult+2
    if k<n:
        k=i*i*i+2
        mult=mult+2
        add=add+1

print("k is {}".format(k))
print("l is {}".format(l))
print("mult is {}".format(mult))
print("add is {}".format(add))
