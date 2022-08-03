# @Time : 2022-08-02 10:53
# @Author : Phalange
# @File : 插入排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


def sort(arr:List):
    """
    选择排序,从小到大的顺序
    :param arr:
    :return:
    """
    if len(arr) == 1:
        return arr
    for i in range(1,len(arr)):
        for j in range(i,0,-1):# 包含i
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break #认为排序好了
        print(arr)


    return arr






if __name__ == "__main__":
    arr = [1,4,2,3,8,5,7,6]
    arr = sort(arr)
    print(arr)