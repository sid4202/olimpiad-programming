class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return l1

        if l1 is None and l2 is not None:
            return l2

        if l2 is None and l1 is not None:
            return l1

        if l1.val < l2.val:
            new_list = ListNode(l1.val)
            new_list_head = new_list
            l1 = l1.next

        elif l2.val < l1.val:
            new_list = ListNode(l2.val)
            new_list_head = new_list
            l2 = l2.next

        elif l2.val == l1.val:
            new_list = ListNode(l1.val)
            next_node = ListNode(l2.val)
            new_list.next = next_node
            l1 = l1.next
            l2 = l2.next
            new_list_head = new_list
            new_list = new_list.next

        while l1 is not None or l2 is not None:
            if l1 is None:
                new_list.next = ListNode(l2.val)
                l2 = l2.next
                new_list = new_list.next
                continue

            if l2 is None:
                new_list.next = ListNode(l1.val)
                l1 = l1.next
                new_list = new_list.next
                continue

            if l1.val < l2.val:
                next_node = ListNode(l1.val)
                new_list.next = next_node
                l1 = l1.next
                new_list = new_list.next
                continue

            if l2.val < l1.val:
                next_node = ListNode(l2.val)
                new_list.next = next_node
                l2 = l2.next
                new_list = new_list.next
                continue

            if l1.val == l2.val:
                next_node = ListNode(l1.val)
                next_node.next = ListNode(l2.val)
                new_list.next = next_node
                l2 = l2.next
                l1 = l1.next
                new_list = new_list.next.next
                continue

        return new_list_head
