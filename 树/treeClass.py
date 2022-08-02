# @Time : 2022-07-31 17:09
# @Author : Phalange
# @File : treeClass.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class BinaryTree:

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.leftChild = self.leftChild
            self.leftChild = tmp
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            tmp = BinaryTree(newNode)
            tmp.rightChild = self.rightChild
            self.rightChild = tmp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key



def preorder(tree:BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree:BinaryTree):
    if tree !=None:
        postorder(tree.getRightChild())
        postorder(tree.getLeftChild())
        print(tree.getRootVal())


def inorder(tree:BinaryTree):
    if tree !=None:
        inorder(tree.getLeftChild())
        inorder(tree.getRootVal())
        print(tree.getRightChild())




if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.getRootVal())
    r.insertLeft('b')
    print(r.getLeftChild())