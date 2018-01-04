# Owen Fish
# 703-915-1306
# fish.owenc@gmail.com

class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._leftChild = None
      self._rightChild = None
      self._height = 1

  def __init__(self):
    self._root = None
    # TODO complete initialization
    
  def findSmallestValue(self, root):
    curr = root
    while curr._leftChild is not None:
      curr = curr._leftChild    
    return curr._value

  def updateHeight(self, node):
    current = node
    if current._leftChild is not None and current._rightChild is not None:
      if current._leftChild._height > current._rightChild._height:
        current._height = current._leftChild._height + 1
      else:
        current._height = current._rightChild._height  + 1
               
    elif current._leftChild is None and current._rightChild is not None:
      current._height = current._rightChild._height + 1     
                    
    elif current._leftChild is not None and current._rightChild is None:
        current._height = current._leftChild._height + 1 
    else:
      current._height = 1
  
  def nodebalance(self, t):

    if t._leftChild is not None and t._rightChild is not None:
      return t._rightChild._height - t._leftChild._height
    if t._leftChild is None and t._rightChild is not None:
      return t._rightChild._height
    if t._leftChild is not None and t._rightChild is None:
      return 0 - t._leftChild._height
    else:
      return 0
    
  
  def _balance(self, t):
    balance = self.nodebalance(t)
    
    if balance == 0 or balance == 1 or balance == -1:
      return t
    
    elif balance == 2:

      if t._rightChild is not None and self.nodebalance(t._rightChild) > 0:

        
        floater = t._rightChild._leftChild
        newroot = t._rightChild
        newroot._leftChild = t
        newroot._leftChild._rightChild = floater
        if t is self._root:
          self._root = newroot
        
        
        self.updateHeight(t)  
        self.updateHeight(newroot)
        return newroot
        
      elif t._rightChild is not None and self.nodebalance(t._rightChild) < 0:

        
        b = t._rightChild
        c = b._leftChild
        floater = c._rightChild
        t._rightChild = c
        c._rightChild = b
        b._leftChild = floater
        
        self.updateHeight(b)
        self.updateHeight(c)
        
        newroot = c
        floater = newroot._leftChild
        newroot._leftChild = t
        t._rightChild = floater
        if t is self._root:
          self._root = newroot
        
        self.updateHeight(t)
        self.updateHeight(newroot)
        
        return newroot
        
    elif balance == -2:


      if t._leftChild is not None and self.nodebalance(t._leftChild) < 0:
      #Single
        floater = t._leftChild._rightChild
        newroot = t._leftChild
        newroot._rightChild = t
        newroot._rightChild._leftChild = floater
        if t is self._root:
          self._root = newroot
          
        self.updateHeight(t)  
        self.updateHeight(newroot)
        
        return newroot
      
      elif t._leftChild is not None and self.nodebalance(t._leftChild) > 0:
      #Double

        b = t._leftChild
        c = b._rightChild
        floater = c._rightChild
        t._leftChild = c
        c._leftChild = b
        b._rightChild = floater
        
        self.updateHeight(b)
        self.updateHeight(c)
        
        
        newroot = c
        floater = newroot._rightChild
        newroot._rightChild = t
        t._leftChild = floater
        if t is self._root:
          self._root = newroot
          
        self.updateHeight(t)
        self.updateHeight(newroot)
        return newroot  

      
      
      
      
      
      
      
      
   
  def _recInsert(self, node, value):
    if self._root is None:
      self._root = self._BST_Node(value)
      return self._balance(self._root)
    
    current = node
    
    if current is None:
      new = self._BST_Node(value)
      current = new
      return self._balance(new)
    
    elif current._value > value:
      current._leftChild = self._recInsert(current._leftChild, value)
      
      self.updateHeight(current)
      return self._balance(current)
    
    elif current._value < value:
      current._rightChild = self._recInsert(current._rightChild, value)
      self.updateHeight(current)
      return self._balance(current)
    
    else:
      raise ValueError
  
  def insert_element(self, value):
    self._recInsert(self._root, value)

#------------------------------------------------------------------------------

  def _recDelete(self, node, value):
    #BASE CASE
    if value == node._value:
      if node._leftChild is None and node._rightChild is None:
        if node is self._root:
          self._root = None
        self.updateHeight(node)  
        return None
      elif node._leftChild is None and node._rightChild is not None:
        if node is self._root:
          self._root = node._rightChild
        self.updateHeight(node)  
        return node._rightChild
      elif node._leftChild is not None and node._rightChild is None:
        if node is self._root:
          self._root = node._leftChild
        self.updateHeight(node)  
        return node._leftChild 
      elif node._leftChild is not None and node._rightChild is not None:
        smallestValue = self.findSmallestValue(node._rightChild)
        node._value = smallestValue
        node._rightChild = self._recDelete(node._rightChild, smallestValue)
        self.updateHeight(node)
        return node
      
    elif value < node._value:
      if node._leftChild is None:
        raise ValueError
      
      node._leftChild = self._recDelete(node._leftChild, value)
      self.updateHeight(node)
      return node
    
    elif value > node._value:
      if node._rightChild is None:
        raise ValueError
      
      node._rightChild = self._recDelete(node._rightChild, value)
      self.updateHeight(node)
      return node
    
  
  def remove_element(self, value):
    # Remove the value specified from the tree
    if self._root is None:
      raise ValueError
    else:
      self._recDelete(self._root, value)
#------------------------------------------------------------------------------

  def rec_in_order(self, node):
    returnStr = ''
    
    if self._root is None:
      return ' '
    
    #recur down to base case:
    if node._leftChild is None:
      returnStr += str(node._value)
      #return returnStr
    
    else:
      returnStr = self.rec_in_order(node._leftChild)
      returnStr += ', ' + str(node._value)
      
    if node._rightChild is not None:
      returnStr += ', ' + str(self.rec_in_order(node._rightChild))
    
    return returnStr

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree.
    if self._root is None:
      return '[ ]'
    else:
      return '[ ' + self.rec_in_order(self._root) + ' ]'

#------------------------------------------------------------------------------

  def rec_pre_order(self, node):
    returnStr = ''
    
    if self._root is None:
      return ''
    
    returnStr += str(node._value)
    if node._leftChild is not None:
        returnStr += ', ' + str(self.rec_pre_order(node._leftChild))
    if node._rightChild is not None:    
        returnStr += ', ' + str(self.rec_pre_order(node._rightChild))
    
    return returnStr

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. 
    if self._root is None:
      return '[ ]'
    else:
      return '[ ' + str(self.rec_pre_order(self._root)) + ' ]'
#------------------------------------------------------------------------------

  def rec_post_order(self, node):
    returnStr = ''
        
    if self._root is None:
      return ''
    
    if node._leftChild is not None:
      returnStr += str(self.rec_post_order(node._leftChild)) + ', '
    if node._rightChild is not None:
      returnStr += str(self.rec_post_order(node._rightChild))+ ', '
    returnStr += str(node._value)   
    return returnStr    

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. 
    if self._root is None:
      return '[ ]'
    else:
      return '[ ' + str(self.rec_post_order(self._root)) + ' ]'

  def __str__(self):
    return self.in_order()

  def get_height(self):
    if self._root is None:
      return 0
    else:
      return self._root._height

if __name__ == '__main__':
  bst = Binary_Search_Tree()
  bst.insert_element(50)
  bst.insert_element(40)
  bst.insert_element(30)
  
  
  
  print('ROOT: ' + str(bst._root._value))
  if bst._root._rightChild is None:
    print('RIGHT CHILD: None')
  else:  
    print('RIGHT CHILD: ' + str(bst._root._rightChild._value))
  if bst._root._leftChild is None:
    print('LEFT CHILD: None')
  else:  
    print('LEFT CHILD: ' + str(bst._root._leftChild._value))
  print()
  print('IN-ORDER: ' + str(bst.in_order()))
  print('PRE-ORDER: ' + str(bst.pre_order()))
  print('POST-ORDER: ' + str(bst.post_order()))  
  print('HEIGHT: ' + str(bst.get_height()))
  
  
  
  
  
  pass #unit tests make the main section unnecessary.
