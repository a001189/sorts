#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 13:40
# @Author  : ysj
# @Site    :
# @Software: PyCharm
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
def bubble_sort(lt):
    """
    两层循环理解：
    第一层 为n-1次 ，每完成一轮循环可完成找到一个最值，找到所有的最值，即完成排序需要n-1轮（n个值，只要一次找到n-1个最值，即可完成）
    第二层 n-k次, 每轮找到一个最值需要就行的交换次数，如第1轮需要n-1次 ；
    :param lt:
    :return:
    """
    list_ = lt.copy()
    n = len(list_)
    count = 0
    for k in range(1, n):  # 第一层 为n-1次
        for j in range(0, n-k):  # 第二层 n-k次
            count += 1
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_, count

# 改进版增加标记


@time_use
def bubble_sort2(lt):
    """
    两层循环理解：
    第一层 为n-1次 ，每完成一轮循环可完成找到一个最值，找到所有的最值，即完成排序需要n-1轮（n个值，只要一次找到n-1个最值，即可完成）
    第二层 n-k次, 每轮找到一个最值需要就行的交换次数，如第1轮需要n-1次 ；
    :param lt:
    :return:
    """
    list_ = lt.copy()
    n = len(list_)
    count = 0
    for k in range(1, n):  # 第一层 为n-1次
        flag = 1  # 标记 如果一轮循环都没改变 说明排序已完成，直接返回
        for j in range(0, n-k):  # 第二层 n-k次
            count += 1
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
                flag = 0
        if flag:
            return list_, count
    return list_, count

@time_use
def bubble_sort3(lt):
    """
    两层循环理解：
    第一层 为n-1次 ，每完成一轮循环可完成找到一个最值，找到所有的最值，即完成排序需要n-1轮（n个值，只要一次找到n-1个最值，即可完成）
    第二层 n-k次, 每轮找到一个最值需要就行的交换次数，如第1轮需要n-1次 ；
    优化 在flag标记的基础上 记录最后一次交换的位置，则下轮交换只需进行到该位置即可
    :param lt:
    :return:
    """
    list_ = lt.copy()
    n = len(list_)
    count = 0
    pos = n - 1
    for k in range(1, n):  # 第一层 为n-1次
        flag = 0
        for j in range(0, pos):
            count += 1
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                pos = j
                flag = 1
        if not flag:
            return list_, count
    return list_, count


@time_use
def raw_sort(*args):
    return sorted(*args)




import random
lists = random.choices(range(1000), k=3000)
# lists = [10000] + list(range(10000))
print(lists)


sort_list, count = bubble_sort(lists)
print(sort_list)
print(count)
print(sort_list == sorted(lists))
print('-' * 50)
print(lists)
sort_list2, count2 = bubble_sort2(lists)
print(sort_list2)
print(count2)
print(sort_list2 == sorted(lists))
print('-' * 50)
sort_list3, count3 = bubble_sort3(lists)
print(sort_list3)
print(count3)
print(sort_list3 == sorted(lists))
raw_sort(lists)
