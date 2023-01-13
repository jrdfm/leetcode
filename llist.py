#!/usr/local/bin/python 

# Defining the Node Class
class ListNode:
    def __init__(self, x): 
        self.val = x
        self.next = None 
  
# Defining the Linked List Class 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
  
        # Allocate the Node & 
        # Put in the data 
        new_node = ListNode(new_data) 
  
        # Make next of new Node as head 
        new_node.next = self.head 
  
        # Move the head to point to new Node 
        self.head = new_node 
  
    # Function to print the linked list 
    def print_list(head):
        # ls = [] 
        temp = head 
        while(temp): 
            print (temp.val) 
            temp = temp.next 
        # print(ls)
  
# Code execution 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    # Insert 6.  So,linked list becomes 6->None 
    llist.push(6) 
  
    # Insert 7 at the beginning. 
    # So linked list becomes 7->6->None 
    llist.push(7) 
  
    # Insert 1 at the beginning. 
    # So linked list becomes 1->7->6->None 
    llist.push(1) 
  
    print ('Created Linked List is:')
    llist.print_list() 
