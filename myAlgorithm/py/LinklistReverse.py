class LinkList:
    def __init__(self, val):
        self.val = val
        self.next = None


class Reverse:
    def reverseLinkedList(self,root):
        if not root or root.next is None:
            return root
        head = self.reverseLinkedList(root.next)
        node = root.next
        node.next = root
        root.next = None
        return head

    def printList(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        strs = "->".join(str(i) for i in res)
        return strs


if __name__ == "__main__":
    list = LinkList(1)
    list.next = LinkList(2)
    list.next.next = LinkList(3)
    list.next.next.next = LinkList(4)
    lst = Reverse().printList(list)
    print lst
    test = Reverse().reverseLinkedList(list)
    test2 = Reverse().printList(test)
    print test2