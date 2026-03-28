def task_c() -> None:
    print("========================================")
    print("==========   Task C: filter   ==========")
    print("========================================")

    data = [5, 10, 15, 20]
    
    even_numbers = list(filter(lambda x: x % 2 == 0, data))
    greater_than_10 = list(filter(lambda x: x > 10, data))
    
    print(f"Original data: {data}")
    print(f"Even numbers: {even_numbers}")
    print(f"Numbers > 10: {greater_than_10}\n")