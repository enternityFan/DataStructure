# @Time : 2022-08-02 11:01
# @Author : Phalange
# @File : 归并排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
from typing import List


def MergeSort1(arr):
    """
    递归方法实现
    :param arr:
    :return:
    """

    if arr == [] or len(arr) < 2:
        return
    process(arr,0,len(arr)-1)

def process(arr,L,R):
    """
    arr[L...R]的范围内变的有序
    :param arr:
    :param L:
    :param R:
    :return:
    """
    if L == R:
        return
    mid = L + ((R - L) >> 1)
    process(arr,L,mid)
    process(arr,mid+1,R)
    merge(arr,L,mid,R)



def merge(arr:List,L:int,mid:int,R:int) -> List:
    p1 = L
    p2 = mid+1
    i = 0
    help = [0] * (R-L+1)
    while p1 <=mid and p2 <=R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 +=1
        else:
            help[i] = arr[p2]
            p2 +=1

        i+=1
    while p1 <=mid:
        help[i] =arr[p1]
        i+=1
        p1 +=1
    while p2 <=R:
        help[i] = arr[p2]
        i+=1
        p2 +=1
    arr[L:R+1] = help
    print(arr)


def MergeSort2(arr):
    """
    非递归实现
    :param arr:
    :return:
    """
    if arr == [] or len(arr) < 2:
        return
    N = len(arr)
    mergeSize = 1 #merge的size
    while mergeSize < N:
        L = 0
        while L < N:
            M = L + mergeSize - 1 # 左组结尾的位置
            if M >=N:
                break
            R = min(N-1,M+mergeSize)
            merge(arr,L,M,R)
            L = R+1

        if (mergeSize > N//2):
            break
        mergeSize <<=1



if __name__ == "__main__":
    arr = [1,4,2,3,8,5,7,6]
    #MergeSort1(arr)
    MergeSort2(arr)
    print(arr)
