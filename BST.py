import math
from tkinter import messagebox
class BinarySearchTree(object):
    def __init__(self, data=None, left=None, right=None, parent=None, Nodelevel=0, centerX=0, centerY=0,circle = None,text = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.centerX = centerX
        self.centerY = centerY
        self.Nodelevel = Nodelevel
        self.circle = []
        self.text = []
        self.line = []
        

class BST(object):
    def __init__(self, elem=None):
        self.root = BinarySearchTree(data=elem)
        self.size = 0
        self.level = 0
        self.Numbers = []
        self.finded = False
    def Arrange_Numbers(self, a):
        if len(a) == 0:
             return
        a_len = len(a)
        n = (a_len - 1) // 2    #εδΈεζ΄
        self.Numbers.append(a[n])
        self.Arrange_Numbers(a[0:n])
        self.Arrange_Numbers(a[n + 1:len(a)])
        
    def lenght(self):
        return self.size

    def find(self, key):
        if self.root:
            result = self._find(key, self.root)
            if result:
                return result
            else:
                return None
        else:
            None
    
    def _find(self, key, node):
        if not node:
            return None
        elif node.data == key:
            return node
        elif key < node.data:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)
        
    def insert(self, key):
        node = BinarySearchTree(key)
        if not self.root:
            self.root = node
            self.size += 1
        else:
            currentNode = self.root
            while True:
                if key < currentNode.data:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = node
                        node.parent = currentNode
                        self.size += 1
                        break
                elif key > currentNode.data:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = node
                        node.parent = currentNode
                        self.size += 1
                        break
                else:
                    break
   
    def findMin(self):
        if self.root:
            return self._findMin(self.root)
        else:
            return None
    
    def findMax(self):
        if self.root:
            currentNode = self.root
            while currentNode.right:
                currentNode = currentNode.right
            return currentNode
        else:
            return None

    def _findMin(self, node):
        if node:
            currentNode = node
            while currentNode.left:
                currentNode = currentNode.left
            return currentNode

    def deleteNode(self, root: BinarySearchTree, key: int) -> BinarySearchTree:
        if root is None:
            return None
        if root.data == key:
            self.finded = True
            if root.left is None:
                if root.right is None: #ζ ε­θηΉοΌη΄ζ₯ε ι€
                    return None
                else:
                    root = root.right #εͺζε³εΏε­θηΉοΌη¨ε³εΏε­ζΏζ’
            elif root.right is None:
                root = root.left #εͺζε·¦εΏε­θηΉοΌη¨ε·¦εΏε­ζΏζ’
            else:
                buffer = None #bufferη¨δΊε­ζΎθ¦ζΏζ’θηΉηηΆθηΉ
                tmp = root.right
                while tmp.left is not None:
                    buffer = tmp
                    tmp = tmp.left
                root.data, tmp.data = tmp.data, root.data
                if buffer is None: #bufferδΈΊη©ΊοΌεrootηε³εΏε­ε³ζ―η?ζ ζΏζ’θηΉ
                    root.right = self.deleteNode(tmp, key)
                else:
                    buffer.left = self.deleteNode(tmp, key)
        elif key < root.data:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def printTree(self):
        if self.size == 0:
            messagebox.showwarning(title='ζη€ΊοΌ', message='ε½εζ δΈΊη©ΊοΌ')
        else:
            self._printTree(self.root)

    def _printTree(self, node):
        if node: #δΈ­εΊιε
            self._printTree(node.left)
            print(node.data)
            self._printTree(node.right)

    def LevelOrder(self):
        self.level = 0
        pRoot = self.root
        if not pRoot:
            return []
        queue = []
        queue.append(pRoot)
        outList=[]
        while queue:
            res=[]
            nextQueue=[]
            for point in queue:     #θΏιειεζ―δΈε±
                res.append(point)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            outList.append(res)
            self.level = self.level + 1
            queue = nextQueue
        self.root.Nodelevel = self.level    
        return outList

    def Create_BST(self):
        self.root.data = self.Numbers[0]
        self.root.centerX = 615
        self.root.centerY = 65
        for temp in self.Numbers[1:]:
            self.insert(temp)
        return self.root

    def Calc_Show_BST(self,root):
            """εεΊιεθ?‘η?ζ―δΈͺηΉηεζ """
            if root == None:
                return
            if root.left:
                root.left.centerX = root.centerX - 20 * (2**(root.Nodelevel-1))
                root.left.centerY = root.centerY + 100
                root.left.Nodelevel = root.Nodelevel -1
                self.Calc_Show_BST(root.left)
            if root.right:
                root.right.centerX = root.centerX + 20 * (2**(root.Nodelevel-1))
                root.right.centerY = root.centerY + 100
                root.right.Nodelevel = root.Nodelevel -1
                self.Calc_Show_BST(root.right)            
