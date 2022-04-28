class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(self, head):
    if head is None:
        return False

    if head.next is None:
        return False

    if head.next.next is None:
        return False

    x1 = head
    x2 = head

    while x1 is not None and x2 is not None:
        if x1.next is None:
            return False

        if x2.next is None:
            return False

        x1 = x1.next
        x2 = x2.next.next

        if x1 == x2 and x2.next.next is not None:
            return True


    return False