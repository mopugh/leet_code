from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head_flag = True

        while True:
            # Handle update
            carry, val = (l1.val + l2.val) // 10, (l1.val + l2.val) % 10
            new_node = ListNode(val)
            if head_flag == True:
                head = new_node
                tail = new_node
                head_flag = False
            else:
                tail.next = new_node
                tail = new_node
            # Handle next iteration
            if l1.next is None and l2.next is None:
                if carry == 0:
                    return head
                l1 = ListNode(carry)
                l2 = ListNode(0)
            elif l1.next is None:
                l2 = l2.next
                l1 = ListNode(carry)
            elif l2.next is None:
                l1 = l1.next
                l2 = ListNode(carry)
            else:
                l1 = l1.next
                l2 = l2.next
                l1.val += carry

        # while True:
        #     # Move up a node
        #     l1_head = ListNode()
        #     l2_head = ListNode()

def print_list(l1):
    while l1.next is not None:
        print(l1.val,end = ' ')
        l1 = l1.next
    print(l1.val)


if __name__ == '__main__':
    l1 = ListNode(9)
    l2 = ListNode(3)
    l2.next = ListNode(2)
    sol = Solution()
    l3 = sol.addTwoNumbers(l1,l2)
    # print(l3.next)
    print('l1: ',end=' ')
    print_list(l1)
    print('l2: ',end=' ')
    print_list(l2)
    print('l3: ',end=' ')
    print_list(l3)
            