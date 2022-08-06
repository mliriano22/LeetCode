# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        m=dummy
        
        while list1 and list2:
            if list1.val < list2.val:

                m.next=list1
                list1=list1.next

            else:

                m.next=list2
                list2=list2.next
                
            m=m.next
            
        if list1:
            m.next=list1
        elif list2:
            m.next=list2
            
            
        return dummy.next
            
              
                
                
        