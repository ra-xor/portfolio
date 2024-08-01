class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LikedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    new_node = Node(val) # create a new node with the appending value
    if not self.head: # if no head ( empty list ), assign the new node as head
      self.head = new_node
      return
    current_node = self.head # if the list has nodes, start from the head
    while current_node.next: # loop thru the list till reach last node
      current_node = current_node.next
    current_node.next = new_node # append the new node as next for current last node

  def reverse(self):
    prev_node = None # initiate prev with None
    current_node = self.head # start with the list head node
    while current_node: # loop thru the list till reach last node
      next = current_node.next # save the next node in next
      current_node.next = prev_node # assign the current note next pointer to the prev
      prev_node = current_node # change the prev to currnet
      current_node = next # change the current to next
    self.head = prev_node # assign list head to the last node
  
  def print(self):
    current_node = self.head # start from the head node
    while current_node: # loop thru all nodes
      print(current_node.val) # print the current node val
      current_node = current_node.next # mode to the next node
