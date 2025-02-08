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
def mergeTwoLists(self, list1, list2): # given two linked lists heads
    # if one of the lists is empty return the other this will work for the case where both are empty
    if not list1 or not list2: 
        if not list2:
            return list1
        else:
            return list2

    # dummy node to start the list this dummy node will be the head of the list and is equal to the smallest value of the two lists
    # since we git our first node for the sorted list we can move to the next node in the list that we got the first node from
    if list1.val <= list2.val:
        dummy = list1
        list1 = list1.next
    else:
        dummy = list2
        list2 = list2.next

    temp = dummy # temp node to keep track of the last node in the list we cannot lose dummy as it is the head of the list
    # while we have nodes in both lists we compare the two nodes and add the smaller one to the list
    while list1 and list2: 
        # if list1 is smaller we add it to the list
        if list1.val <= list2.val:
            temp.next = list1 # add the node to the list
            list1 = list1.next # move to the next node in the list
            temp = temp.next # move the temp node to the next node in the list (the one we just added)
        else:
            # if list2 is smaller we add it to the list
            temp.next = list2 # add the node to the list
            list2 = list2.next # move to the next node in the list
            temp = temp.next # move the temp node to the next node in the list (the one we just added)
        
    # if we have nodes left in one of the lists we add them to the list by assigning temp.next to the remaining list, the list with no next node is linked
    # the other node. Note that since we said while list1 and list2 once we exit the loop one of the lists will be empty hence we cannot do list1.next or list2.next
    # we must use temp.next which still points to the last node in the list.
    if list1: # if list1 is not empty
        temp.next = list1 # add the remaining nodes from list1 to the list
    else: # if list2 is not empty
        temp.next = list2 # add the remaining nodes from list2 to the list

    return dummy # return the head of the list



    