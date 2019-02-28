"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Steven Pham
ID:      180198020
Email:   pham8020@mylaurier.ca
__updated__ = "2019-01-21"
-------------------------------------------------------
"""

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(s, a):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(s, a)
    -------------------------------------------------------
    Parameters:
        s - a Stack object (Stack)
        a - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for x in range(len(a),0,-1):
        s.push(a.pop())

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    """
    while stack.is_empty() == False:
        target.insert(0,stack.pop())
        
        
        
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """   
    s = Stack()
    array_to_stack(s, source)
    print(s.is_empty())
    print(s.peek())
    print(s.pop())
    print(s.push(2))
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) != 0:
        removed = source.pop(0)
        queue.insert(removed)
        
        
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while queue.is_empty() == False:
        
        target.insert(len(target),queue.remove())
    

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) != 0:
        removed = source.pop(0)
        pq.insert(removed)
        

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while pq.is_empty() == False:
        
        target.insert(len(target),pq.remove())
        
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    q = Queue()

    array_to_queue(q, a)
    print(q.is_empty())
    print()
    print(q.insert(a))
    print()
    print(q.remove())
    print()
    print(q.peek())
    
    
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    print(pq.is_empty())
    print()
    print(pq.insert(a[2]))
    print()
    print(pq.peek())
    print()
    print(pq.remove())

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        llist.append(source.pop(0))
        
    

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.insert(0,llist.pop())
    
def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print(lst.is_empty())
    for value in a:
        lst.insert(0,value)
        
    print(lst.peek())
    print(lst.remove(a[2]))
    print(lst.find(a[3]))
    print(lst.index(a[1]))
    print(lst.count(a[4]))
    print(lst.append(a[2]))
    print(lst.max())
    print(lst.min())
    print(lst.__getitem__(a[1]))
    print(lst.__setitem__(0, a[1]))
    print(lst.__contains__(a[1]))
    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return

        