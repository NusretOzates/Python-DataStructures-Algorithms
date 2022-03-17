def fibonacci(n: int, memory: dict):
    if n in memory:
        return memory[n]
    if n <= 2:
        return 1
    memory[n] = fibonacci(n - 1, memory) + fibonacci(n - 2, memory)
    return memory[n]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(45))
