class LinkList(object):

    def __init__(self, root=0):
        self.value = root
        self.next = None

    def printLinkedList(self, val):
        if val:
            if val.next:
                print(val.value)
                self.printLinkedList(val.next)
            else:
                print(val.value)
        return


def oddEvenList(head: LinkList) -> LinkList:
    if head and head.next:
        odd = head
        even = LinkList(odd.next.value)
        even_head = even
        odd.next = odd.next.next
        odd = odd.next if odd.next else odd
        while (odd and odd.next):
            node = LinkList(odd.next.value)
            odd.next = odd.next.next
            even.next = node
            odd = odd.next if odd.next else odd
            even = even.next
        odd.next = even_head
    return head

ll = LinkList(1)
ll.next = LinkList(2)
ll.next.next = LinkList(3)
ll.next.next.next = LinkList(4)
ll.next.next.next.next = LinkList(5)
ll.next.next.next.next.next = LinkList(6)

a = oddEvenList(ll)
ll.printLinkedList(a)