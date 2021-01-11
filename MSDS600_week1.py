a = 4
b = 2
c = a + b
d = a * b

item1 = 'python'
item2 = 'is'
item3 = 'fun'
item4 = '!'

np.random.randint(0, 100,(5,2))

e = pd.Series([1,3,5,np.nan,6,8])


def fibonacci (x):
    if x > 1:
        x = fibonacci(x-1) + fibonacci(x-2)
    return(x)
    
fib = []
iteration = 20
for i in range(0, iteration):
    fib.append(fibonacci(i))
print(fib)

x = list(range(iteration))

plt.plot(x, fib)
plt.xlabel('Iteration Length')
plt.ylabel("Fibonacci's Values")
plt.title ("Fibonacci Sequence")
plt.show()

def fibo(num):
    a, b = 0, 1
    for i in range(0, num):
        yield a
        a, b = b, a + b
        
l = list(fibo(20))

plt.plot(l)
plt.xlabel('Iteration Length')
plt.ylabel("Fibonacci's Values")
plt.title ("Fibonacci Sequence")
plt.show()



# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Thu Jan 30 23:57:12 2020)---
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')

## ---(Fri Jan 31 00:02:14 2020)---
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
import pandas
pandas.__version__

## ---(Mon Feb  3 21:38:57 2020)---
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
x*y
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
x*y
x*y
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')
x*y
x*y/z
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')
x*y/z
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')

## ---(Thu Feb  6 13:41:27 2020)---
runfile('C:/Users/megal/.spyder-py3/untitled0.py', wdir='C:/Users/megal/.spyder-py3')
runfile('C:/Users/megal/.spyder-py3/untitled1.py', wdir='C:/Users/megal/.spyder-py3')

## ---(Thu Feb  6 13:45:24 2020)---
runfile('C:/Users/megal/untitled1.py', wdir='C:/Users/megal')

## ---(Mon Feb 10 17:35:05 2020)---
runfile('C:/Users/megal/untitled1.py', wdir='C:/Users/megal')

## ---(Tue Feb 11 11:37:14 2020)---
runfile('C:/Users/megal/untitled0.py', wdir='C:/Users/megal')
runfile('C:/Users/megal/untitled2.py', wdir='C:/Users/megal')

## ---(Sun Apr 12 18:59:03 2020)---
runfile('C:/Users/megal/Desktop/GIS4810/Python/Lab3.py', wdir='C:/Users/megal/Desktop/GIS4810/Python')

## ---(Sun Apr 12 19:44:42 2020)---
runfile('C:/Users/megal/Desktop/ScriptL3.py', wdir='C:/Users/megal/Desktop')

## ---(Tue Nov 17 06:16:28 2020)---
runfile('C:/Users/megal/tfintro.py', wdir='C:/Users/megal')

## ---(Wed Nov 18 14:51:34 2020)---
runfile('C:/Users/megal/tfintro.py', wdir='C:/Users/megal')

## ---(Wed Nov 18 21:44:13 2020)---
runfile('C:/Users/megal/tfintro.py', wdir='C:/Users/megal')
runfile('C:/Users/megal/Desktop/TensorFlow/tf_second.py', wdir='C:/Users/megal/Desktop/TensorFlow')
predictions[0]
np.argmax(predictions[0])
nm.argmax(predictions[0])
test_labels[0]
runfile('C:/Users/megal/Desktop/TensorFlow/tf_second.py', wdir='C:/Users/megal/Desktop/TensorFlow')
img = test_images[1]

print(img.shape)
# Add the image to a batch where it's the only member.
img = (nm.expand_dims(img,0))

print(img.shape)
runfile('C:/Users/megal/Desktop/TensorFlow/tf_second.py', wdir='C:/Users/megal/Desktop/TensorFlow')
nm.argmax(predictions_single[0])

## ---(Sun Jan  3 12:33:26 2021)---
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
x+y+z
x*y-z

## ---(Mon Jan 11 08:30:18 2021)---
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
c
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
d
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
a++d/b
a==d/b
print (item1, item2, item3, item4)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
print (item1, item2, item3, item4)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
np.random.randint(0, 100,(5,2))
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
e
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
e
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
e
e[3]
e[0]
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
e
e.dropna()
def add_two_numbers (a, b)
def add_two_numbers(a, b):
    return a+b
    
add_two_numbers (2,4)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
fibonacci(12)
fibonaci (12)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
fibonacci(12)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
x
plt.plot(x, fib)
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')
l
runfile('C:/Users/megal/.spyder-py3/temp.py', wdir='C:/Users/megal/.spyder-py3')