#!/usr/local/bin/python 



'''There is a singly-linked list head and we want to delete a node node in it.
    You are given the node to be deleted node. You will not be given access to 
    the first node of head.'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    nxt = node.next
    node.next = nxt.next
    node.val = nxt.val
    del(nxt)


def removeNthFromEnd(head, n):
    cur = head
    ls = []
    while cur.next != None:
        ls.append(cur)
        cur = cur.next
    if cur == head:
        del(head)
        return None
    else:
        ls.append(cur)
    node = ls[-n]
    if node == head:
        head = node.next
        del(node)
    else:
        ls[-n - 1].next = node.next
        del(node) 
    return head

'''chatGpt arguably better'''
def removeNthFromEnd(head, n): 
    # Setting two pointers: slow_ptr and fast_ptr 
    slow_ptr = head
    fast_ptr = head 
    
    # Moving fast_ptr n nodes ahead of slow_ptr 
    for _ in range(n - 1): 
        fast_ptr = fast_ptr.next
  
    # If fast_ptr reaches the end of the linked list, then the node to be deleted is the head of the linked list
    if not fast_ptr: 
        del(head)
        return None
    # Move slow_ptr and fast_ptr at the same speed
    # until fast_ptr reaches the end of the linked list
    while fast_ptr and fast_ptr.next:
        prev = slow_ptr 
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    # Delete the node at slow_ptr
    if slow_ptr == head:
        head = slow_ptr.next
        del(slow_ptr)
    else: 
        prev.next = slow_ptr.next
        del(slow_ptr) 
  
    return head 
'''Given the head of a singly linked list, reverse the list, and return the reversed list'''

def reverseList(head):
    cur = head
    prev = None
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev 

def print_list(head):
    # ls = [] 
    temp = head 
    while(temp): 
        print (temp.val) 
        temp = temp.next 
if __name__ == '__main__':
    from llist import *
    head = []
    head = [1,2,3,4,5]
    # head = [1]
    # head = [1,2]
    llist = LinkedList() 
    for i in head[::-1]:
        llist.push(i)
    print_list(llist.head)
    # print(llist.head.val)
    # print(f'cur {cur.val}, prev {prev.val}, next {nxt.val}')
    
    print_list(reverseList(llist.head))