#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
import sys
sys.setrecusionlimit(1000000)

def mergeLists(head1, head2):
    # both the list are NULL
    if head1 == None and hear2 == None:
        return None
    # only one list is NULL
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
        # general logic
        temp = None
        if head1.data < head2.data:
            temp = head1
            temp.next = mergeLists(head1.next, head2)
        else:
            temp = head2
            temp.next = mergeLists(head1, head2.next)
            
        return temp


if __name__ == '__main__':
