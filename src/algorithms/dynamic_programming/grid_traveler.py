def grid_travel(r: int, c: int, memory: dict):
    if f"{r},{c}" in memory:
        return memory[f"{r},{c}"]
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1

    memory[f"{r},{c}"] = grid_travel(r - 1, c, memory) + grid_travel(r, c - 1, memory)

    return memory[f"{r},{c}"]


print(grid_travel(18, 18, {}))
