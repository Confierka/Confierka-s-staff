from math import *
import matplotlib.pyplot as plt

N=100
def freq(x):
    return sin(2*pi*x)

def A(k):
    if k==0:
        return 0
    return log(k)


def f(x):
    result=0
    for k in range(N//2):
        result +=A(k)*freq(k*x)
    return result
    

x_array = [i/N for i in range(N)]
y_array = [f(x) for x in x_array]

X_array = [0.0 for i in range(N)]
X_array_i=[0.0 for i in range(N)]

omega_array=[]
h_array = []

for k in range (N//2):
    omega=2*pi*k/N
    
    for n in range(N):
        X_array[k] += y_array[n]*cos(omega*n)
        X_array_i[k]-=y_array[n]*sin(omega*n)
    x=X_array[k]
    y=X_array_i[k]

    omega_array.append(k)
    h_array.append(sqrt(x**2+y**2)/N)

plt.plot(omega_array,h_array)
plt.xscale('log')

#plt.plot(x_array,y_array)
plt.show()