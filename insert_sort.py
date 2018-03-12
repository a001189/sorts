#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 13:38
# @Author  : ysj
# @Site    : 
# @File    : insert_sort.py
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
def insert_sort(lt):
    """
    插入排序, 未考虑数据结构稳定性，即 列表 两个相同元素的相对位置可能在排序后发生变化
    :param lt:
    :return:
    """
    list_ = list()
    list_.append(lt[0])  # 首次先放入一个值，节省时间
    for value in lt[1:]:
        if value <= list_[0]:  # 最小值则，插入行首
            list_.insert(0, value)
            continue
        if value >= list_[-1]:  # 最大值则，添加行尾 （原因，负索引无法插入最后一位）
            list_.append(value)
            continue
        for check_index in range(-2, -len(list_), -1):  # 倒序比较，上述两个判断已排除列表收尾，故从
            if value >= list_[check_index]:
                list_.insert(check_index+1, value)  # 负索引，故其后插入，要+1
                break
        else:  # 值在第0位，第1位之间的情况
            list_.insert(1, value)
    return list_


# import random
# for k in random.choices(range(1, 1000), k=1000):
#     lists = random.choices(range(1000), k=k)
#     # lists = [10000] + list(range(10000))
#     # lists = [871, 44, 254, 40]
#     # print(lists)
#     # print('sort')
#     # sort_list = select_sort(lists)
#     # print(sort_list)
#     # print(sort_list == sorted(lists))
#     # print('-' * 50)
#     sort_list2 = insert_sort(lists)
#     # print(sort_list2)
#     if sort_list2 != sorted(lists):
#         print(lists)


# lists = [622, 644, 273, 592, 655]
# sort_list2 = insert_sort(lists)
# print(sort_list2)
# print(sort_list2 == sorted(lists), )
