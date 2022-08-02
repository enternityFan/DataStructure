# @Time : 2022-07-31 17:16
# @Author : Phalange
# @File : 解析树构建器.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import operator

from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    """

    :param fpexp: "(3+2)*(5+(3/2))
    :return: Tree
    """
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-/*)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i== ')':
            currentTree

        else:
            raise ValueError("Unknown Operator: " + i)
    return eTree


def evaluate(parseTree:BinaryTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


print(evaluate(buildParseTree('( 3 + ( 4 * 5 ) )')))