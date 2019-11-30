class NodeList:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getStartPoint(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return False
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow.val


