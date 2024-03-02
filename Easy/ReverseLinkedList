def reverse_linked_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head # new node points to first node 
    prev = None # inittily theres no prevoius node to the first node
    while current is not None:
        new_node = current.ref #  to get our newnode "the node after first node which is current" we use the current nodes refrence witch points us to the next node, after frist iteration current is prev our last moved node now this node stores the refrence to get us to our next node
        current.ref = prev # let this selected node be moves to a spot prevous "behind" the current first node, in the second iteration since current was node last moved we move our new mode behind the prevously moved node
        prev = current # that node we just moved to prev is now our currrent node becuse we will need its ref later 
        current = new_node # that current node is our new node becuse of the first line it pulls currents refrence we have to let our newly moved node ("prev" thats = current) be our new node so we can take its refrence and go to next node
    # head = prev # remember how the head points to the first node to start with, when we are done reversing our last node moved "prev" is now our first node so let the head point to new first node
    
    return prev

"""
# NOTE in a linked list you should let head = prev see comment on why but in the leetcode solution return prev 
# as leetcode only wants the first node of the linked list which too start was your first node so to check if your correct
# it just wants your last node to check if you reversed it properly
"""

# Initial Linked List: 1 2 3 4 5 # prev the node behind 1 is none

# After First Iteration: 2 1 3 4 5 # prev is now 2 and node 2s ref will point us to 3

# After Second Iteration: 3 2 1 4 5

# After Third Iteration: 4 3 2 1 5

# After Fourth Iteration: 5 4 3 2 1

# After Fifth Iteration (Final Result): 5 4 3 2 1 # see how the prev "last node" to be moved is 5 this was originally our first node now its our las this is what leetcode checks