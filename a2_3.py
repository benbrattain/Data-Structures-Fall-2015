#--- Part III: implement cyclic lists; implement the Josephus problem

from lec2 import *

class CyclicList :

  """Similar in spirit to the class MutableList but the list MAY contain cycles.
  >>> xs = CyclicList()
  >>> xs.add(1)
  >>> xs.add(2)
  >>> xs.add(3)
  >>> xs.add(4)
  >>> xs.add(5)
  >>> xs.take(10)
  [5, 4, 3, 2, 1]
  >>> xs.take(2)
  [5, 4]
  >>> xs.hasLoop()
  False
  >>> xs.setTail(5,1)
  >>> xs.take(12)
  [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4]
  >>> xs.hasLoop()
  True
  >>> xs.setTail(5,2)
  >>> xs.take(12)
  [5, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 2]
  >>> xs.hasLoop()
  True
  """

  def __init__(self) :
    self.front = EmptyList()

  def p(self, i = -1):
    temp = self.front
    ls = []
    while i != 0 and not temp.isEmpty():
      ls.append(temp.head)
      temp = temp.tail
      i -= 1
    return ls

  def add (self,v) :
    self.front = self.front.add(v)

  def next (self) :
    """Adjusts the front pointer to point to the tail."""
    self.front = self.front.tail

  def singleton (self) :
    """Returns True or False depending on whether the list has exactly one element
    or not.
    >>> xs = CyclicList()
    >>> xs.add(5)
    >>> xs.singleton()
    True
    >>> xs = CyclicList()
    >>> xs.add(5)
    >>> xs.setTail(1,1)
    >>> xs.singleton()
    True
    >>> xs = CyclicList()
    >>> xs.singleton()
    False
    >>> xs = CyclicList()
    >>> xs.add(5)
    >>> xs.add(6)
    >>> xs.singleton()
    False
    >>> xs = CyclicList()
    >>> xs.add(5)
    >>> xs.add(6)
    >>> xs.setTail(2,1)
    >>> xs.singleton()
    False
    """
    if self.front.isEmpty() :
      return False
    return self.front.tail.isEmpty() or self.front.tail == self.front

  def deleteIth (self, i) :
    temp = self.front
    while i > 0:
      temp = temp.tail
      i -= 1
    self.front = temp.tail
    return temp.head
    # return temp.head
    
  def deleteNext (self) :
    """Deletes the next node. Returns the contents of the deleted node.
    >>> xs = CyclicList()
    >>> xs.add(1)
    >>> xs.add(2)
    >>> xs.add(3)
    >>> xs.add(4)
    >>> xs.take(10)
    [4, 3, 2, 1]
    >>> xs.next()
    >>> xs.take(10)
    [3, 2, 1]
    >>> xs.deleteNext()
    2
    >>> xs.take(10)
    [3, 1]
    """
    temp = self.front.tail
    self.front.tail = temp.tail
    return temp.head

  def take (self,i) :
    """Traverses the current object and collects the elements in a Python list. If the
    current object does not have a cycle and has fewer than 'i' elements, the result
    is just the elements in the current list. If the current object contains more than
    'i' elements or is cyclic, only the first 'i' elements are collected."""
    temp = list()
    pointer = self.front
    while not pointer.isEmpty() and i != 0:
      temp.append(pointer.head)
      pointer = pointer.tail
      i -= 1
    return temp

  def setTail (self,j,i) :
    """Set the tail pointer of the 'j'th node (counting from 1) to point to
    the 'i'th node (again counting from 1). If i <= j, this will create a
    cycle in the list."""
    pointerOne = self.front
    pointerTwo = self.front
    while i > 1 and not pointerOne.isEmpty():
      pointerOne = pointerOne.tail
      i -= 1
    while j > 1 and not pointerTwo.isEmpty():
      pointerTwo = pointerTwo.tail
      j -= 1
    pointerTwo.tail = pointerOne

  def hasLoop (self) :
    """Detects if the current list has a loop."""
    if self.front.isEmpty() :
      return False
    else :
      firstPointer = self.front
      secondPointer = firstPointer.tail
      while firstPointer != secondPointer :
        if firstPointer.isEmpty() or secondPointer.isEmpty() or secondPointer.tail.isEmpty():
          return False
        secondPointer = secondPointer.tail
        if firstPointer == secondPointer:
          return True
        firstPointer = firstPointer.tail
        secondPointer = secondPointer.tail
      return True
    
  def isEmpty (self) :
    return self.front.isEmpty()

#---

class Josephus :

  def __init__ (self,n,k) :
    """The parameter 'n' is the number of people; they are numbered 1 to n;
    the parameter 'k' is the count used at each step where k-1 people are skipped
    and the k'th person is executed.
    >>> Josephus(5,2).people.take(12)
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
    """
    self.n = n
    self.k = k
    self.people = CyclicList()
    for i in range(n,0,-1) :
      self.people.add(i)
    self.people.setTail(n,1)

  def skip(self,i) :
    """Moves the pointer to 'people' by 'i' steps.
    >>> j = Josephus(5,2)
    >>> j.people.take(12)
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2]
    >>> j.skip(3)
    >>> j.people.take(12)
    [4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    >>> j.skip(3)
    >>> j.people.take(12)
    [2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
    >>> j.skip(3)
    >>> j.people.take(12)
    [5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
    """
    pointer = self.people.front
    while i > 0 :
      pointer = pointer.tail
      i -= 1
    self.people.front = pointer

  def simulate(self,i) :
    """Start the simulation from person number 'i'
    >>> j = Josephus(10,2)
    >>> j.simulate(3)
    8
    >>> j = Josephus(20,7)
    >>> j.simulate(1)
    4
    """
    self.skip(i)
    while not self.people.singleton() :
      # print self.people.take(20)
      self.skip(self.k - 2)
      self.people.deleteNext()
      self.skip(1)
    return self.people.front.head
 
#-----------------------------------------------------------------------------

if __name__ == "__main__" :
  import doctest
  doctest.testmod()


