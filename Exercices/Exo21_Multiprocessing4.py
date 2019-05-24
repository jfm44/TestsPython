import concurrent.futures as cf

def compute (data):
    a,b = data
    return a + b

with cf.ThreadPoolExecutor(3) as executor:
    print(list(executor.map(compute,[(1,2),(7,-4),(9,3)])))