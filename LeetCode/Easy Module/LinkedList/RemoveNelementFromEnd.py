from LinkedListPack.LinkedList import LinkList

def removeNelement(value, n):
    fast_pointer = value
    slow_pointer = value
    i = 0
    while i < n:
        fast_pointer = fast_pointer.next
        i += 1

    if not fast_pointer:
        return slow_pointer.next

    while fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    slow_pointer.next = slow_pointer.next.next
    return value



ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(10)
ll.next.next.next = LinkList(70)
ll.next.next.next.next = LinkList(90)


a = removeNelement(ll, 4)
ll.printLinkedList(a)
