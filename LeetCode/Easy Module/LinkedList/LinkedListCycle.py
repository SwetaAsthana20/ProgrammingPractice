from LinkedListPack.LinkedList import LinkList


def hasCycle(head: LinkList) -> bool:
    if head and head.next:
        fast_pointer = head.next
        slow_pointer = head

        while fast_pointer.next and fast_pointer.next.next and slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return bool(slow_pointer == fast_pointer)
    else:
        return False


ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(10)
ll.next.next.next = LinkList(70)
ll.next.next.next.next = ll

a = hasCycle(ll)
print(a)