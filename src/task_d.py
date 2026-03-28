def task_d() -> None:
    print("==============================================")
    print("=  Task D: map/filer vs list comprehensions  =")
    print("==============================================")

    data = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # using map + filter
    map_filter_result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, data)))
    
    # using list comprehension
    comprehension_result = [x * x for x in data if x % 2 == 0]
    
    print(f"Original data: {data}")
    print(f"Result using map/filter: {map_filter_result}")
    print(f"Result using comprehension: {comprehension_result}\n")