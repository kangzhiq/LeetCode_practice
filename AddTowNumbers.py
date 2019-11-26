# Add Two Numbers

"""
Created on Sat Nov 26 11:09:55 2019

@author: zhiqi
"""

# Update 26/11/2019
# Runtime 68 ms
# Beats 90.96%

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val is None:
            return l2
        if l2.val is None:
            return l1
        head = l1
        carry = 0
        # Adding l2 to l1
        while l1.next is not None:
            if l2.next is None:
                break
            temp_carry = (l1.val + l2.val + carry) // 10
            l1.val = (l1.val + l2.val + carry) % 10
            carry = temp_carry
            print(l1.val)
            print(carry)
            l1 = l1.next
            l2 = l2.next
        
        if l1.next is None and l2.next is None:
            if l1.val + l2.val + carry >= 10:
                l1.val = (l1.val + l2.val + carry) % 10
                l1.next = ListNode(1)
            else:
                l1.val = l1.val + l2.val + carry
        
        elif l1.next is None:
            temp_carry = (l1.val + l2.val + carry) // 10
            l1.val = (l1.val + l2.val + carry) % 10
            carry = temp_carry
            l2 = l2.next
            l1.next = l2
            while l2.next is not None:
                temp_carry = (l2.val + carry) // 10
                l2.val = (l2.val + carry) % 10
                carry = temp_carry
                l2 = l2.next
            if carry + l2.val == 10:
                l2.val = 0
                l2.next = ListNode(1)
            else:
                l2.val = l2.val + carry
                
        elif l2.next is None:
            temp_carry = (l1.val + l2.val + carry) // 10 
            l1.val = (l1.val + l2.val + carry) % 10      
            carry = temp_carry
            l1 = l1.next
            while l1.next is not None:
                temp_carry = (l1.val + carry) // 10
                l1.val = (l1.val + carry) % 10
                carry = temp_carry
                l1 = l1.next
            if carry + l1.val == 10:
                l1.val = 0
                l1.next = ListNode(1)
            else:
                l1.val = l1.val + carry
        return head
