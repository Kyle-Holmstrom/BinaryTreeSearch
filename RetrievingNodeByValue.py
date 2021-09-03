class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None
    
  # Insert a value into the Binary Search Tree  
  def insert(self, value):
    if value < self.value:    # Checks that target value is less than root's value
      if self.left is None:   # Checks that left node doesn't exist
        self.left = BinarySearchTree(value, self.depth + 1)  # if left node doesn't exist we instantiate BinarySearchTree with target value and a depth one greater than self.depth and assign this to our self.left node
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)  # if node already exist we insert our new value into the node
    else:
      if self.right is None:  # Checks that right node doesn't exit
        self.right = BinarySearchTree(value, self.depth + 1)  # if right node doesn't exist we instantiate BinarySearchTree with target value and a depth one greater than self.depth and assign this to our self.right node
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)  # if node already exist we insert our new value into the node

  # Retrieve Node by value  
  def get_node_by_value(self, value):
    if value == self.value:  # Compares target value to self
      return self  # If they are the same, we found target node so we return self
    elif self.left and value < self.value:  # Check left node for target value
      return self.left.get_node_by_value(value) # If target value exist in left node make a recursive call to get_node_by_value()
    elif self.right and value > self.value:  # Check right node for target value
      return self.right.get_node_by_value(value)  # If target value exist in right node make a recursive call to get_node_by_value()
    else:
      return None  # If none of the previous conditions are True then target value does not exist in Binary Search Tree.. we return None   
  
root = BinarySearchTree(100)  # Instantiate BinarySearchTree with a default value of 100

# insert data into root with our insert() method
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

# Get nodes by value below:
print(root.get_node_by_value(75).value)
print(root.get_node_by_value(55))