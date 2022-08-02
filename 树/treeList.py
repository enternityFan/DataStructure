# @Time : 2022-07-31 17:00
# @Author : Phalange
# @File : treeList.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



def BinaryTree(r):
    return [r,[],[]]



def insertLeft(root,newBranch):
    """
    用来插入左子树
    :param root:根节点
    :param newBranch:新的分支
    :return:
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):
    """
    用来插入右子树
    :param root:根节点
    :param newBranch:新的分支
    :return:
    """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]


def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    r = BinaryTree(3)
    print(insertLeft(r,4))
    print(insertLeft(r,5))
    print(insertRight(r,6))
    print(insertRight(r,7))
    print(getLeftChild(r))
    print(setRootVal(getLeftChild(r),9))
