from LinkedListPack.LinkedList import LinkList


def reverseList(head: LinkList) -> LinkList:
    if head and head.next:
        first_pointer = head
        second_pointer = head.next

        first_pointer.next = None

        while second_pointer.next:
            third_pointer = second_pointer.next
            second_pointer.next = first_pointer
            first_pointer = second_pointer
            second_pointer = third_pointer

        second_pointer.next = first_pointer

        return second_pointer

    else:
        return head


ll = LinkList(20)
ll.next = LinkList(50)
ll.next.next = LinkList(10)
ll.next.next.next = LinkList(70)
ll.next.next.next.next = LinkList(90)


a = reverseList(ll)
ll.printLinkedList(a)
