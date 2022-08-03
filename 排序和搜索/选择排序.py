# @Time : 2022-08-02 10:48
# @Author : Phalange
# @File : 选择排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


def sort(arr:List):
    """
    选择排序,从小到大的顺序
    :param arr:
    :return:
    """

    for i in range(len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[len(arr)-i-1]:
                arr[j],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[j]
        print(arr)

    return arr






if __name__ == "__main__":
    arr = [1,4,2,3,8,5,7,6]
    arr = sort(arr)
    print(arr)