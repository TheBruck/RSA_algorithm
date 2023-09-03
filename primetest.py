from math import *
import numpy as np
import numpy.polynomial.polynomial as npol
from random import *
import matplotlib.pyplot as plt
import time

def pgcdeuclide(a,b):
     while b!=0:
         r=a%b
         a,b=b,r
     return a

def primetest(p):#On test si les entiers donnés en entrée sont premier
     boo=True
     if boo:
         for i in range(2,int(sqrt(p))+1):
             if p%i==0:
                 boo=False
     return(boo)

def largestprimefactor(n):
     l=[]
     d=2
     if n==1:
         return(1)
     while n%d==0:
         l.append(d)
         q=int(n/d)
         n=q
     d=3
     while d<=n:
         while n%d==0:
             l.append(d)
             q=int(n/d)
             n=q
         d+=2
     return(max(l))
def formab(n,a):
     b=2
     p=a**b
     while p<=n:
         if p==n:
             return(True)
         b+=1
         p=a**b
     return(False)

def primetestaks1(n):
     r=2
     while r<n :
         if pgcdeuclide(n,r) != 1:
             return(False)
         elif primetest(r):
             q=largestprimefactor(r-1)
             if q>=4*sqrt(r)*log(n) and (n**((r-1)/q)%r)!=1:
                 break
         r+=1
     PR=npol.Polynomial([-1]+[0 for k in range(r-1)]+[1])
     for a in range(int(2*sqrt(r)*log(n))):
         P=(npol.polypow([a,1],n))
         Q=(npol.Polynomial([-1]+[0 for k in range(n-1)]+[1]))
         if a!=1 and formab(n,a):
             return(False)
         elif npol.Polynomial(((P%PR).coef)%n)!=npol.Polynomial(Q.coef):
             return(False)
     return(True)

def testordre(n):
     lim=4*log2(n)**2
     boo= False
     r=1
     while not boo:
         r+=1
         k=1
         boo=True
         while k<lim and boo:
             k+=1
             if (n**k)%r in (0,1):
                 boo=False
     return(r)

def phi(n):
     phi=0
     for d in range(1,n):
         if pgcdeuclide(n,d)==1:
            phi+=1
     return(phi)

def primetestaks2(n):
     if n==1:
         return(False)
     r=testordre(n)
     for a in range(2,r+1):
         if 1<pgcdeuclide(n,a)<n:
             return(False)
     if n<=r:
         return(True)
     PR=npol.Polynomial([-1]+[0 for k in range(r-1)]+[1])
     for a in range(1,int(2*sqrt(phi(r))*log2(n))):
         P=(npol.Polynomial([a,1],n))
         Q=(npol.Polynomial([-1]+[0 for k in range(n-1)]+[1]))
         if npol.Polynomial(((P%PR).coef)%n)!=npol.Polynomial(((Q%PR).coef)%n):
             return(False)
     return(True)

def millerrabin(n):
     if n == 2 or n ==3 :
         return True
     if n % 2 == 0:
         return False
     s, m = 0, n - 1
     while m % 2 == 0:
         s += 1
         m //= 2
     for a in range(1,int(2*log(n)**2)):
         boo=False
         if (a**m)%n==1:
             boo=True
         for r in range(s - 1):
             x = (a**((2**r)*m))%n
             if x == n - 1:
                boo=True
         if not boo:
             return False
     return True

X=[]
Y1=[]
Y2=[]
Y3=[]
for i in range(2,1000):
    tref=time.process_time()
    X.append(i)
    primetest(i)
    t=time.process_time()
    Y1.append(t-tref)

for i in range(2,1000):
    tref=time.process_time()
    X.append(i)
    primetestaks1(i)
    t=time.process_time()
    Y2.append(t-tref)

for i in range(2,1000):
    tref=time.process_time()
    X.append(i)
    millerrabin(i)
    t=time.process_time()
    Y3.append(t-tref)

plt.plot(X,Y1)
plt.plot(X,Y2)
plt.plot(X,Y3)
plt.xlabel('entiers testés')
plt.ylabel('temps d éxécution')
plt.show()

print('fini le tipe')

