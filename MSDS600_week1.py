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
