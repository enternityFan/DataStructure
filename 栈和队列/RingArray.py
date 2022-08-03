# @Time : 2022-08-02 8:16
# @Author : Phalange
# @File : RingArray.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class RingArray:
    def __init__(self,limit):
        self.arr = [0] * limit
        self.pushi = 0
        self.polli = 0
        self.size = 0
        self.limit = limit

    def push(self,value):
        if self.limit == self.size:
            print("栈满了！")
            return
        self.size +=1
        self.arr[self.pushi] = value
        self.pushi = self.nextIndex(self.pushi)

    def pop(self):
        if  self.size==0:
            print("栈空的")
            return
        self.size -=1
        ans = self.arr[self.polli]
        self.polli = self.nextIndex(self.polli)
        return ans

    def isEmpty(self):
        return self.size == 0

    def nextIndex(self,i):
        return i+1 if i < self.limit - 1  else 0



if __name__ == "__main__":
    arr = RingArray(3)
    print(arr.isEmpty())
    arr.push(1)
    arr.push(2)
    arr.push(3)
    arr.push(4)
    arr.pop()
    arr.push(2)
    print(arr)


