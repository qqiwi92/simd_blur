import time
import os
import resource
from contextlib import contextmanager

@contextmanager
def perf_measure(label):
    start_time = time.perf_counter()
    start_res = resource.getrusage(resource.RUSAGE_SELF)
    
    yield
    
    end_time = time.perf_counter()
    end_res = resource.getrusage(resource.RUSAGE_SELF)
    
    print(f"\n{'=' * 10} {label} {'=' * 10}")
    print(f"Чистое время: {end_time - start_time:.4f} сек")
    print(f"CPU Time: {end_res.ru_utime - start_res.ru_utime:.4f} сек")
    print(f"Page Faults: {end_res.ru_minflt - start_res.ru_minflt}")