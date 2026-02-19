# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create dummy head
        head = ListNode()
        cur = head

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # Attach remaining nodes
        cur.next = list1 or list2

        return head.next


# Helper function to create linked list from Python list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Helper function to print linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# -------------------------
# Testing the solution
# -------------------------

# Create linked lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([2, 3])

# Merge lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Print result
print_linked_list(merged_list)
