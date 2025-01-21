# given the head of a LL check if it has a cycle, meaning if if the tail (last node) points back to any node in the LL
""" 
SOL: loop through the LL until we we get to the tail, we dont know that this is the tail but here we check:
    1) if the current node points back to the intial node (given head) 
    2) if the current node points back to a node we have seen before
    - in these 2 cases we know there is a cycle and return true
    3) if we get to the end of the LL meaning the last ref is none then there is no cycle we return false 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(head) -> bool:
    temp = head # store teh first node (the initial head given to us) in a temp variable 
    seen = [] # create a list to track nodes we have seen
    n = head # start at the head
    if n is None: return False # if the LL is empty return false as the next line will try to access n.next which will throw an error as there no n
    while n.next is not None: # loop through the LL until we get to the tail (the last node)
        if n.next == temp or n in seen: # at some point we will reach the last node i.e n will be the last node, then we check if the last node points back to the first node (temp) or if the last node has been seen before
            return True # if either of these 2 conditions are met we return True as there is a cycle
        seen.append(n) # after traversing each node we add it to the seen list
        n = n.next # move to the next node
    return False # if we break out of the loop i.e we get to this line then n.next was none meaning the tail points to none and there is no cycle so we return False