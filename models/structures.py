class Node:
    """ This class represents a node in the tree """
    def __init__(self, val):
        self.value = val.person_id
        self.content = val
        self.leftChild = None
        self.rightChild = None
    
    def insert(self, data):
        if self.value == data.person_id:
            return False

        elif self.value > data.person_id:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
        
    def find_by_id(self, id):
        if(self.value == id):
            return self.content
        elif self.value > id:
            if self.leftChild:
                return self.leftChild.find_by_id(id)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find_by_id(id)
            else:
                return False
        
    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getSize() + self.rightChild.getSize()
        elif self.leftChild:
            return 1 + self.leftChild.getSize()
        elif self.rightChild:
            return 1 + self.rightChild.getSize()
        else:
            return 1

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find_by_id(self, id):
        if self.root:
            return self.root.find_by_id(id)
        else:
            return False
      
    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0
      
    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0
  
    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node  
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None


class Queue(object):
    def __init__(self):
        self.elements = []

    def dequeue(self):
        return self.elements.pop(0)

    def enqueue(self, val):
        self.elements.append(val)

    def peek(self):
        if len(self.elements) > 0:
            return self.elements[0]
        return False
        

class QueueItem:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = [0]

    def enqueue(self, val, priority):
        data = QueueItem(val, priority)
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) < 2:
           return False 
        return self.heap[1]
        
      
    def dequeue(self):
        if len(self.heap) < 2: 
            return False
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        return max.val

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index].priority > self.heap[parent].priority:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if (
            len(self.heap) > left and 
            self.heap[largest].priority < self.heap[left].priority):
            largest = left
        if (len(self.heap) > right and 
            self.heap[largest].priority < self.heap[right].priority):
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
            