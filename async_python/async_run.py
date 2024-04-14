from concurrent.futures import ThreadPoolExecutor, as_completed

def do_some_function(x):
    return (x ** 2) + x


params = [11, 12,13,14,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=4) as executor:
    future = {executor.submit(do_some_function, param) for param in params}
    results = [f.result() for f in as_completed(future)]

    print(results)