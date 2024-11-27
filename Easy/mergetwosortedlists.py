# problem
"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
# ! solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode()
    # Use 'current' to build the merged list starting from the dummy node
    current = dummy

    # Loop until one of the lists is fully traversed
    while list1 and list2:
        # Compare the current values of list1 and list2
        if list1.val <= list2.val:
            # If list1's value is smaller, attach list1's node to the merged list
            current.next = list1
            # Move to the next node in list1
            list1 = list1.next
        else:
            # If list2's value is smaller, attach list2's node to the merged list
            current.next = list2
            # Move to the next node in list2
            list2 = list2.next
        # Move the 'current' pointer forward in the merged list
        current = current.next

    # If list1 is not empty, attach the remaining nodes of list1
    # Otherwise, attach the remaining nodes of list2
    current.next = list1 if list1 else list2

    # Return the merged list, starting from the node after the dummy
    return dummy.next