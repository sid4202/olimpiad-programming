class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def find_linked_list_nodes(self, head):
        visited = []
        x1 = head
        while x1 is not None:
            if x1.val in visited:
                return visited
            else:
                visited.append(x1.val)
                x1 = x1.next
        return visited

    def detectCycle(self, head):
        if head is None:
            return -1
        if head.next is None:
            return -1
        if head.next.next is None:
            return -1
        x1 = head
        x2 = head
        nodes = self.find_linked_list_nodes(head)
        while x1 is not None and x2 is not None:
            if x1.next is None:
                return -1
            if x2.next is None:
                return -1
            x1 = x1.next
            x2 = x2.next.next
            if x1 == x2 and x2.next.next is not None:
                print(nodes)
                print(x1.val)
                print(nodes.index(x1.val))
                return nodes.index(x1.val)
        return -1
