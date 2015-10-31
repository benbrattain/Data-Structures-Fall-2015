#Assumption about Binary Search Tree:
#Method of storing is if integer is less than node, go left
#if greater than or equal to node, go right.
#Stating this clearly just in case my assumption is wrong so you know my logic
#(I dont think it is)
"""
* Here is a template for a tree implementation using the interpreter
  design pattern

* Keep the implementation immutable (persistent)

* Add a method 'size' that counts the number of nodes in a tree

* Assuming the tree is maintained as a (non-necessarily balanced) BST
  holding integers, write the methods 'insert', 'delete', and 'search'. 

* Write methods 'inorder', 'preorder', and 'postorder' to traverse the 
  tree and return a list of the values encountered in the relevant
  traversal.

* Write a function 'sort' that uses the BST as an intermediate step:
  as discussed in class, it inserts the elements of the list in the BST
  and then traverses the tree 'inorder'.
  
* Implement the following two rotations of a tree:
  - right rotation takes a tree that must look like:

             Q
           /   \
          P     C
        /  \
       A   B

    where A, B, and C are arbitrary subtrees; the result of the
    rotation is the tree:

             P
           /   \
          A     Q
              /  \
             B    C

   - left rotation does the inverse operation
                          
* Write a function that reconstructs a tree from its preorder and inorder
  traversals

* Write a function that reconstructs a tree from its postorder and inorder
  traversals

* Write a function that reconstructs a tree from a list containing
  an arithmetic expression in postfix notation. For example, the list
  [4,5,'*',2,'+',8,1,'+','/']
  would produce the tree:
  ((4 * 5) + 2) / (8 + 1)

"""

from random import *

class Tree :
  pass

class Empty (Tree) :
  def show (self,indent) :
    return ' '*indent + '*'

  def height (self) :
      return 0

class Node (Tree) : 
  def __init__ (self,val,left,right) :
    self.val = val
    self.left = left
    self.right = right

  def show (self,indent) :
    return ' '*indent + str(self.val) + '\n' + \
           self.left.show(indent+2) + '\n' + \
           self.right.show(indent+2)

  def height (self) :
      return 1 + max (self.left.height(), self.right.height())

def Leaf (v) : 
  return Node(v,Empty(),Empty())

def generate (h) : 
  if h == 0 : 
    return Empty()
  else :
    return Node(randrange(100),generate(h-1),generate(h-1))

def display (t) :
  print (t.show(0))

def size (t) :
  if isinstance(t, Empty) :
    return 0
  return 1 + size(t.left) + size(t.right)

def insert(t, v) :
  if isinstance(t, Empty) :
    return Leaf(v)
  if t.val > v :
    return Node(t.val, insert(t.left, v), t.right)
  else :
    return Node(t.val, t.left, insert(t.right, v))

def delete(t, v) :
 
  def transplant(t) :
    if isinstance(t.left, Empty) and isinstance(t.right, Empty):
      return Empty()
    if isinstance(t.left, Empty):
      return Node(t.right.val, t.left, transplant(t.right))
    if isinstance(t.right, Empty):
      return Node(t.left.val,transplant(t.left), t.right)
    else :
      return Node(t.right.val, t.left, transplant(t.right))

  if isinstance(t,Empty):
    print "Value not found!"
    return
  if t.val < v :
    return Node(t.val, t.left, delete(t.right, v))
  if t.val > v :
    return Node(t.val, delete(t.left, v), t.right)
  if t.val == v :
    print "Value found!"
    return transplant(t)

def search(t, v) :
  if isinstance(t,Empty):
    print "Value not found!"
    return
  if t.val < v :
    return Node(t.val, t.left, search(t.right, v))
  if t.val > v :
    return Node(t.val, search(t.left, v), t.right)
  if t.val == v :
    print "Value found!"
    return

# Assumption: 1st Left, 2nd Node Value, 3rd Right.
def inorder(t) :
  orderedlist = []
  
  def helper(t) :

    if not isinstance(t, Empty) :
      helper(t.left)
      orderedlist.append(t.val)
      helper(t.right)

  helper(t)
  return orderedlist

# Assumption: 1st node, 2nd left, 3rd right
def preorder(t) :
  orderedlist = []
  
  def helper(t) :

    if not isinstance(t, Empty) :
      orderedlist.append(t.val)
      helper(t.left)
      helper(t.right)

  helper(t)
  return orderedlist


#Assumption: 1st left, 2nd right, 3rd node
def postorder(t) :
  orderedlist = []
  
  def helper(t) :

    if not isinstance(t, Empty) :
      helper(t.left)
      helper(t.right)
      orderedlist.append(t.val)

  helper(t)
  return orderedlist

def sort(ls) :
  tree = Empty()
  for x in ls :
    tree = insert(tree, x)
  return inorder(tree)

def rightrotation(t) :
  return Node(t.left.val, t.left.left, Node(t.val, t.left.right, t.right))

def leftrotation(t) :
  return Node(t.right.val, Node(t.val, t.left, t.right.left), t.right.right)


#sorry about the tons of code here with unneccessary variables.
#i had to write these with nothing to write on and it helped me keep everything straight.
def preorderreconstruct(prels, inls) :
  prestart = 0
  preend = len(prels) - 1
  instart = 0
  inend = len(inls) - 1
  def construct(prels, inls, prestart, instart, preend, inend) :
    if prestart > preend or instart > inend :
      return Empty()

    val = prels[prestart]
    tree = Leaf(val)
    j = 0
    i = 0

    while i < inend + 1:
      if val == inls[i] :
        j = i
        break
      i += 1


    leftinstart = instart
    leftinend = j - 1
    leftprestart = prestart + 1
    leftpreend = prestart + j - instart
    tree.left = construct(prels, inls, leftprestart, leftinstart, leftpreend, leftinend)

    rightinstart = j + 1
    rightinend = inend
    rightprestart = prestart + j - instart + 1
    rightpreend = preend

    tree.right = construct(prels, inls, rightprestart, rightinstart, rightpreend, rightinend)
    
    return tree

  return construct(prels, inls, prestart, instart, preend, inend)


def postorderreconstruct(postls, inls) :
  poststart = 0
  postend = len(postls) - 1
  instart = 0
  inend = len(inls) - 1

  def construct(postls, inls, poststart, instart, postend, inend) :
    if poststart > postend or instart > inend :
      return Empty()

    val = postls[postend]
    tree = Leaf(val)
    j = 0
    i = 0

    while i < inend + 1:
      if val == inls[i] :
        j = i
        break
      i += 1

    leftinstart = instart
    leftinend = j - 1
    leftpoststart = poststart
    leftpostend = poststart + j - instart - 1
    tree.left = construct(postls, inls, leftpoststart, leftinstart, leftpostend, leftinend)

    rightinstart = j + 1
    rightinend = inend
    rightpoststart = poststart + j - instart
    rightpostend = postend - 1

    tree.right = construct(postls, inls, rightpoststart, rightinstart, rightpostend, rightinend)
    
    return tree

  return construct(postls, inls, poststart, instart, postend, inend)

def expressiontree(ls) :
  treestack = list()
  for i in range(0, len(ls)) :
    if not isinstance(ls[i], int) :
      left = treestack.pop()
      right = treestack.pop()
      treestack.append(Node(ls[i], left, right))
    else :
      treestack.append(Leaf(ls[i]))
  return treestack.pop()





if __name__ == "__main__" : 
  t1 = Node('a',Node('b',Empty(),Leaf('d')),Node('c',Leaf('e'),Leaf('f')))
  t2 = generate(2)
  t3 = generate(3)
  t4 = generate(4)
  t5 = Node(5, Node(4, Leaf(3), Leaf(4)), Node(7, Leaf(5), Node(8, Leaf(7), Leaf(10))))
  a = inorder(t1)
  b = preorder(t1)
  c = postorder(t1)
  xs = [5, 7, 17, 21, 42, 1, 9, 7]
