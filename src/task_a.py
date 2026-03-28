def apply(func, data):
    result = []
    for element in data:
        result.append(func(element))
    return result

def task_a() -> None:
    print("========================================")
    print("===   Task A: High-Order Functions   ===")
    print("========================================")

    data = [1, 2, 3]
    result = apply(lambda x: x + 2, data)
    print(f"apply(lambda x: x+2 on {data})  ->  {result}\n")