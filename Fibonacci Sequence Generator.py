def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:-1]

n = int(input("Enter a number: "))
print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")
