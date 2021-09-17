import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Salary_Data.csv")
print(data.columns)
a=data["YearsExperience"]
#print(a,type(a))
b=data["Salary"]
#print(b,type(b))
l1=a.tolist()
print(l1)
l2=b.tolist()
print(l2)

c=sum(l1) # Summation x
print(c)
d=sum(l2) # Summation y
print(d)

pro=[]
for i,j in zip(l1,l2):
    pro.append(i*j)
print(pro)
e=sum(pro) # Summation xy
print(e)


l3=[]
for i in l1:
    l3.append(i*i)
print(l3)


f=sum(l3) # Summation of x^2
print(f)

g=c*c # summation x whole square
print(g)

n=30
m=((n*e)-(c*d))/((n*f)-g) # m= (n*summation(xy)-(summation(x).summation(y)))/ ((n*summation(x^2)-(summation(x))^2)
print(m)

k=(d-(m*c))/n  # c=(summation(y)-m*summation(x))/n
print(k)

for i in x_test:
    y_p=(m*i)+k
    print(y_p)

