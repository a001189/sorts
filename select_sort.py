#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 16:58
# @Author  : ysj

from functools import wraps
import time


def time_use(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('time use %ss' % str(time.time() - start))
        return result
    return wrapper


@time_use
def raw_sort(*args):
    return sorted(*args)

# time_use(raw_sort(*arg))

@time_use
def select_sort(lists):
    """
    依次找每个位置的值（对应的最小值），需要n-1次；如 位置0，则从后续所有的值中找出最小值的位置，然后交换这两个值
    每次找值需要n -k 次
    :param lists:
    :return:
    """
    lt = lists.copy()
    length = len(lt)
    for position in range(length-1):
        min_index = position
        for index in range(position+1, length):
            min_index = index if lt[index] < lt[min_index] else min_index
        lt[position], lt[min_index] = lt[min_index], lt[position]
    return lt


@time_use
def select_sort2(lists):
    """
    依次找每个位置的值（对应的最小值），需要n-1次；如 位置0，则从后续所有的值中找出最小值的位置，然后交换这两个值
    每次找值需要n -k 次
    优化，每次找两个值(最大值，最小值)
    :param lists:
    :return:
    """
    lt = lists.copy()
    tail = count = length = len(lt)
    for position in range(length-1):
        min_index = max_index = position
        for index in range(position+1, tail):
            min_index = index if lt[index] < lt[min_index] else min_index
            max_index = index if lt[index] > lt[max_index] else max_index
        # 修改count < 0  为 <= 0 即可不需要下面判断
        # if tail <= position + 1:  # 循环区域为空，说明所有元素已已就绪，直接返回。
        #     return lt
        lt[position], lt[min_index] = lt[min_index], lt[position]
        if max_index == position:  # 最大值是交换位置时，会被交换上一步交换到最小值的index，so 需要更改位置
            max_index = min_index
        lt[-(position+1)], lt[max_index] = lt[max_index], lt[-(position+1)]
        tail -= 1  # 最大值也找到了，因此后续选择时也要排除该值
        count -= 2
        if count <= 0:  # 一次找两个值，所有的均找到，则count计数为0或-1，终止返回
            print(count)
            return lt
    return lt

import random
for k in random.choices(range(10000), k=40):
    lists = random.choices(range(1000), k=k)
    # lists = [10000] + list(range(10000))
    # lists = [871, 44, 254, 40]
    # print(lists)
    # sort_list = select_sort(lists)
    # print(sort_list)
    # print(sort_list == sorted(lists))
    # print('-' * 50)
    sort_list2 = select_sort2(lists)
    # print(sort_list2)
    print(sort_list2 == sorted(lists), k)
