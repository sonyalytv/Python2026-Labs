def task_b() -> None:
    print("========================================")
    print("===========   Task B: map   ============")
    print("========================================")

    data = [1, 2, 3]
    
    squared_numbers = list(map(lambda x: x * x, data))
    string_numbers = list(map(str, data))
    
    print(f"Original data: {data}")
    print(f"Squared: {squared_numbers}")
    print(f"Converted to strings: {string_numbers}\n")