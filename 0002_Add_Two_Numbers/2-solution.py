# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummyHead is a pointer to the head of the result list
        # the reason why we need a dummyHead is because we don't know the head of the result list yet
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0
        
        # we need to check if l1 or l2 is None because we don't know if l1 or l2 is longer
        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            # this is how we calculate the sum and the carry
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            # create a new node and append it to the result list
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # we need to return the next node of the dummyHead because the dummyHead is not part of the result list
        result = dummyHead.next
        
        # actually it is not necessary to set dummyHead.next to None, because we have already returned the result list
        dummyHead.next = None

        # when we return dummyHead.next, we are returning the first node of the result list, 
        # and each node in the result list points to the next node. It implicitly returns the whole result list.
        return result