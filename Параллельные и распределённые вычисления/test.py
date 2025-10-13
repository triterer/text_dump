#sequential
def f(x):
    return x * x - x + 1

result = 3
for i in range(3):
    result = f(result)

#parallel
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor
import os

def f(x):
    return x * x - x + 1

executor = ThreadPoolExecutor(max_workers=os.cpu_count())
futures = [executor.submit(f, 3) for i in range(3)]
_ = concurrent.futures.as_completed(futures)
executor.shutdown()


#concurrent_eh?
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor
import os

def f(x):
    return x * x - x + 1

core_num = os.cpu_count() if os.cpu_count().is_integer() else 4
executor = ThreadPoolExecutor(max_workers= core_num * 4)
futures = [executor.submit(f, 3) for i in range(3)]
_ = concurrent.futures.as_completed(futures)
executor.shutdown()

#concurent with shared resource
import concurrent.futures
from concurrent.futures.thread import ThreadPoolExecutor
import os

def f(x):
    return x * x - x + 1

def shared_resource_f():
    global interesting_variable
    return f(interesting_variable)

interesting_variable = 3

core_num = os.cpu_count() if os.cpu_count().is_integer() else 4
executor = ThreadPoolExecutor(max_workers=core_num * 4)
futures = [executor.submit(f, _) for i in range(3)]
_ = concurrent.futures.as_completed(futures)
executor.shutdown()

