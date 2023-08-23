#!/usr/bin/python3
from typing import Tuple

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# page_size = 4
# page_number = 5
# start = (page_number -1) * page_size # 1 * 3
# end = start + page_size 

# result = data[start:end]
# print(result)

# print(data[3:6])

def index_range(page: int, page_size: int) -> Tuple:
    start = (page -1) * page_size
    end = start + page_size
    result = start, end
    return tuple(result)

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)