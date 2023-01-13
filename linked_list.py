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

'''Given the head of a linked list, remove the nth node from the end of the list and return its head.'''
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



'''Merge the two lists in a one sorted list.
   Return the head of the merged linked list.'''
# kinda works sometimes
def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    cur1, cur2 = list1, list2
    tmp1, tmp2 = cur1.next, cur2.next
    prev = None
    if cur1.val <= cur2.val:
        head = cur1
        cur1.next = cur2
        prev = cur2
    else:
        head = cur2
        cur2.next = cur1
        prev = cur1
    cur1, cur2 = tmp1, tmp2 

    while cur1 and cur2 and cur1.next and cur2.next:
        tmp1, tmp2 = cur1.next, cur2.next
        if cur1.val <= cur2.val:
            prev.next = cur1
            cur1.next = cur2
            prev = cur2
        else:
            prev.next = cur2
            cur2.next = cur1
            prev = cur1
        cur1, cur2 = tmp1, tmp2

    if cur1 and cur1.next:
        tmp1 = cur1.next
        if cur1.val <= cur2.val:
            prev.next = cur1
            cur1.next = cur2
            cur2.next = tmp1
        else:
            prev.next = cur2
            cur2.next = cur1 
            cur1.next = tmp1

    elif cur2 and cur2.next:
        tmp2 = cur2.next
        if cur2.val <= cur1.val:
            prev.next = cur2
            cur2.next = cur2
            cur2.next = tmp2
        else:
            prev.next = cur1
            cur1.next = cur2 
            cur2.next = tmp2
    else:
        if cur1 and cur1.val <= cur2.val:
            prev.next = cur1
            cur1.next = cur2
        elif cur2:
            prev.next = cur2
            cur2.next = cur1     
           
    return head

# recursion + chatGpt saves the day
# def mergeTwoLists(list1, list2):
#     temp = None
#     if list1 is None:
#         return list2
#     elif list2 is None:
#         return list1
        
#     if list1.val <= list2.val:
#         temp = list1
#         temp.next = mergeTwoLists(list1.next, list2)
#     else:
#         temp = list2
#         temp.next = mergeTwoLists(list1, list2.next)
        
#     return temp

if __name__ == '__main__':
    from llist import *

    def print_list(head):
        ls = [] 
        temp = head 
        while(temp): 
            ls.append(temp.val)
            # print (temp.val) 
            temp = temp.next 
        print(ls)  
    head = []
    head = [1,2,3,4,5]
    # head = [1]
    # head = [1,2]
    # llist = LinkedList() 
    # for i in head[::-1]:
    #     llist.push(i)
    # print_list(llist.head)
    # print(llist.head.val)
    # print(f'cur {cur.val}, prev {prev.val}, next {nxt.val}')
    
    # print_list(reverseList(llist.head))
    # list1 = [1,2,4]
    # list2 = [1,3,4]
    # list1 = []
    # list2 = []
    # list1 = []
    # list2 = [0]
    list1 = [2]
    list2 = [1]
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    for i in list1[::-1]:
        llist1.push(i)

    for i in list2[::-1]:
        llist2.push(i)
    head = mergeTwoLists(llist1.head, llist2.head)
    print_list(head)