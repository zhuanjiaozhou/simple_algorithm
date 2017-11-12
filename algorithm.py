#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

# 获取执行时间


class Timeit(object):

    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        cost = datetime.datetime.now() - start
        print(cost)
        print(ret)
        return ret

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, *args):
        cost = datetime.datetime.now() - self.start
        print(cost)


# 时间复杂度O(n)
@Timeit
def sequential_search(list, key):
    # 最基础的遍历无序列表的查找算法
    time = 0
    for i in range(len(list)):
        time += 1
        if list[i] == key:
            print('seq times: {}'.format(time))
            return i
    print('seq times: {}'.format(time))
    return False


# 时间复杂度O(log(n))
@Timeit
def binary_search(list, key):
    # 针对有序查找表的二分查找算法
    low = 0
    high = len(list) - 1
    time = 0
    while low <= high:
        time += 1
        mid = int((low + high) / 2)
        if mid > high:
            return False
        if key < list[mid]:
            high = mid - 1
        elif key > list[mid]:
            low = mid + 1
        else:
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


# 时间复杂度O(log(n))
@Timeit
def binary_search_value(lis, key):
    # 插值查找算法
    low = 0
    high = len(lis) - 1
    time = 0
    try:
        while low <= high:
            time += 1
            # 计算mid值是插值算法的核心代码
            mid = low + int((high - low) *
                            (key - lis[low]) / (lis[high] - lis[low]))
            # print("mid=%s, low=%s, high=%s" % (mid, low, high))
            if key < lis[mid]:
                high = mid - 1
            elif key > lis[mid]:
                low = mid + 1
            else:
                # 打印查找的次数
                print("times: %s" % time)
                return mid
        print("times: %s" % time)
    except:
        return False


@Timeit
def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


@Timeit
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 5
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


@Timeit
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


@Timeit
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return list


@Timeit
def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

#############
# 堆排序


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    for i in range(0, (size / 2))[::-1]:
        adjust_heap(lists, i, size)


@Timeit
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

#######
# 归并排序


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


@Timeit
def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


import math
# 基数排序


@Timeit
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))  # k获取最大位数
    bucket = [[] for i in range(radix)]  # 生成存放数的radix个桶
    for i in range(1, k + 2):  # 遍历位数，从低到高
        for j in lists:  # 遍历元素
            bucket[j // (radix ** (i - 1)) % radix].append(j)  # 分桶
        del lists[:]
        for z in bucket:
            lists += z  # 合并桶
            del z[:]
    return lists


if __name__ == '__main__':
    LIST1 = [1, 5, 7, 8, 22, 54, 99, 123, 200,
             222, 444, 555, 666, 777, 888, 10000000]

# 查找
    result_sequential = binary_search(LIST1, 22222)
    result_binary = binary_search(LIST1,22222)
    result_value = binary_search_value(LIST1, 22222)


# 排序
    LIST = [100, 5, 999, 8, 22, 54, 99, 66, 200, 199,
            444, 18, 666, 3, 2, 1, 9, 1000, 30, 65, 88, 10]
    result = insert_sort(LIST)
    result_shell = shell_sort(LIST)
    result_bubble = bubble_sort(LIST)
    result_quick = quick_sort(LIST,0,len(LIST)-1)
    result_select = select_sort(LIST)
    result_heap = heap_sort(LIST)
    result_merge = merge_sort(LIST)
    result_radix = radix_sort(LIST,10)
