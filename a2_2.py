#--- Part II: implement stacks using mutable lists; implement queues using two stacks
from a2_1 import * 

class Stack :
    """
    >>> s = Stack()
    >>> s.isEmpty()
    True
    >>> s.push(4)
    >>> s.push('dog')
    >>> s.peek()
    'dog'
    >>> s.push(True)
    >>> s.size()
    3
    >>> s.isEmpty()
    False
    >>> s.push(8.4)
    >>> s.pop()
    8.4
    >>> s.pop()
    True
    >>> s.size()
    2
    """

    def __init__ (self) :
        self.stack = MutableList()

    def isEmpty (self) :
        return self.stack.isEmpty()

    def size (self) :
        return self.stack.size()

    def push (self, v) :
        self.stack.append(v)

    def pop (self) :
        return self.stack.pop()

    def peek (self) :
        node = self.stack.front
        value = node
        i = self.size()
        if node != EmptyList() :
            while i > 0 :
                value = node.head
                temp = node.tail
                node = temp
                i -= 1
            return value

class Queue :
    """
    >>> q = Queue()
    >>> q.isEmpty()
    True
    >>> q.enqueue(4)
    >>> q.enqueue('dog')
    >>> q.enqueue(True)
    >>> q.size()
    3
    >>> q.isEmpty()
    False
    >>> q.dequeue()
    4
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    'dog'
    >>> q.dequeue()
    True
    >>> q.dequeue()
    8.4
    >>> q.size()
    0
    """
    def __init__ (self) :
      self.front = Stack()
      self.back = Stack()
    
    def isEmpty (self) :
        return self.front.isEmpty() and self.back.isEmpty()

    def size (self) :
        x = self.front.size() + self.back.size()
        return x

    def enqueue (self, v) :
        if self.back.isEmpty() :
             self.front.push(v)
        else :
            while self.back.isEmpty() != True :
                value = self.back.peek()
                self.back.pop()
                self.front.push(value)

    def dequeue (self) :
        if self.front.isEmpty() :
            x = self.back.peek()
            self.back.pop()
            return x
        else:
            while self.front.isEmpty() != True :
                value = self.front.peek()
                self.front.pop()
                self.back.push(value)
            x = self.back.peek()
            self.back.pop()
            return x

if __name__ == "__main__" :
  import doctest
  doctest.testmod()
