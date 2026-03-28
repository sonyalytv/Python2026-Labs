import time

def cache(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    return wrapper

def tribonacci_uncached(n, print_calls = False):
    if print_calls:
        print(f"Calculate: {n}")
    if n in (0, 1, 2):
        return n
    return tribonacci_uncached(n - 1, print_calls) + tribonacci_uncached(n - 2, print_calls) + tribonacci_uncached(n - 3, print_calls)

@cache
def tribonacci_cached(n, print_calls = False):
    if print_calls:
        print(f"Calculate: {n}")
    if n in (0, 1, 2):
        return n
    return tribonacci_cached(n - 1, print_calls) + tribonacci_cached(n - 2, print_calls) + tribonacci_cached(n - 3, print_calls)    

def task_g() -> None:
    print("========================================")
    print("=====   Task G: Caching Decorator   ====")
    print("========================================")
    
    small_test = 5
    print("Tribonacci(5)")
    print("Uncached calls:")
    tribonacci_uncached(small_test, True)
    print()
    print("Cached calls:")
    tribonacci_cached(small_test, True)
    print()
    
    test_val = 25
    
    start_time = time.time()
    tribonacci_uncached(test_val)
    uncached_time = time.time() - start_time
    
    start_time = time.time()
    tribonacci_cached(test_val)
    cached_time = time.time() - start_time
    
    print(f"Uncached Tribonacci({test_val}) time: {uncached_time:.5f} seconds")
    print(f"Cached Tribonacci({test_val}) time: {cached_time:.5f} seconds")
    print()