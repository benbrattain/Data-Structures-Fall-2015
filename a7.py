
#-----------------------------------------------------------------------------
# binary heap as discussed in class: each node has at most 2 chidren

#Assuming you want a Min-Heap based off of the functions below. Implemented it this way.
class B_Heap :
    def __init__ (self) :
        self.elems = [None]
        self.size = 0

    def __repr__ (self) :
        return repr(self.elems[1:])

    def isEmpty (self) : 
        return self.size == 0

    def getSize (self) : 
        return self.size

    def findMin (self) :
        self.minHeapify(1)
        return self.elems[1]

    def minHeapify(self, index) :
        if index == 0 or index >= self.size:
            raise IndexError('Invalid index.')
        minimum = self.findMinIndex(index)
        if not minimum == index :
            self.swapElements(index,minimum)
            self.minHeapify(minimum) #continues the heapify progress to make sure the old parent is actually the min

    def swapElements(self, oldIndex, newIndex) :
        oldParent = self.elems[oldIndex]
        newParent = self.elems[newIndex]
        self.elems[oldIndex] = newParent
        self.elems[newIndex] = oldParent

    def findMinIndex(self, index) :
        left = 2 * index
        right = 2 * index + 1
        if left <= self.size and self.elems[left] < self.elems[index] :
            minimum = left
        else : 
            minimum = index
        if right <= self.size and self.elems[right] < self.elems[minimum] :
            minimum = right
        return minimum

    def buildMinHeap(self) :
        self.size = len(self.elems) - 1
        length = len(self.elems) / 2
        for i in range(length, 0) :
            self.minHeapify(i)

    def insert (self,k) :
        self.elems.insert(1,k)
        self.size += 1
        self.minHeapify(1)

    def extractMin (self) : 
        if self.size < 1 :
            raise SizeError('Your heap is too small!')
        minimum = self.elems[1]
        self.elems[1] = self.elems[self.size]
        self.size -= 1
        self.minHeapify(1)
        return minimum

#-----------------------------------------------------------------------------
# d-ary heap: each node has at most d-children

class D_Heap :
    def __init__ (self,d) :
        self.elems = [None]
        self.size = 0
        self.d = d

    def __repr__ (self) :
        return repr(self.elems[1:])

    def isEmpty (self) :
        return self.size == 0

    def getSize (self) : 
        return self.size

    def findMin (self) : 
        self.minHeapify(1)
        return self.elems[1]

    def insert (self,k) : 
        self.elems.insert(1,k)
        self.size += 1
        self.minHeapify(1)

    def extractMin (self) : 
        if self.size < 1 :
            raise SizeError('Your heap is too small!')
        minimum = self.elems[1]
        self.elems[1] = self.elems[self.size]
        self.size -= 1
        self.minHeapify(1)
        return minimum

#------------------------------------------------------------------------------
# Implementing binary heap using trees; swap subtrees to maintain shape!

class B_Heap_Tree () : pass

class Empty (B_Heap_Tree) :
    def __repr__ (self)     : return '_'

    def isEmpty (self) : pass
    def getSize (self) : pass
    def findMin (self) : pass
    def insert (self,k) : pass
    def extractMin (self) : pass


class Node (B_Heap_Tree) :
    def __init__ (self,val,left,right) :
        self.val = val
        self.left = left
        self.right = right

    def __repr__ (self) :
        return '[{},{},{}]'.format(self.val,self.left,self.right)

    def isEmpty (self) : pass
    def getSize (self) : pass
    def findMin (self) : pass
    def insert (self,k) : pass
    def extractMin (self) : pass

#-----------------------------------------------------------------------------
