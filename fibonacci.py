# fibonacci.py
def fib(limit=100):
    a, b = 0, 1
    while a <= limit:
        yield a, a ** 2
        a, b = b, a + b

for f in fib():
    if f > 100:
        break
    print(f)

# Add line 1
# Add line 2
# Add line 3
