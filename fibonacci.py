# fibonacci.py
def fib(limit=100):
    a, b = 0, 1
    while a <= limit:
        yield a, a ** 2
        a, b = b, a + b

def main():
    print("Fibonacci sequence (with squares) up to the limit:")
    for f, f_square in fib():
        print(f"{f} (Square: {f_square})")

if __name__ == "__main__":
    main()
